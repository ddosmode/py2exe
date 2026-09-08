#!/usr/bin/env python3
"""Переводит docstrings и комментарии в Python-файлах на русский язык.

Использование:
    python3 translate_docs.py [--dry-run] [директория]

Флаг --dry-run выводит изменения без записи в файлы.
Если директория не указана, используется текущая директория."""

import ast
import functools
import io
import os
import re
import sys
import tokenize
from pathlib import Path

_translate_fn = None


@functools.lru_cache(maxsize=512)
def translate_text(text):
    """Переводит текст на русский язык. Результат кэшируется."""
    fn = get_translator()
    return fn(text)


def _init_github_models():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise ImportError("GITHUB_TOKEN не найден в env")
    from openai import OpenAI
    client = OpenAI(api_key=token, base_url="https://models.github.ai/", timeout=30.0)

    def _gh(text):
        if not text or not text.strip() or len(text) < 3:
            return text
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Переведи следующий текст на русский язык. Сохраняй технические детали, имена переменных, код и форматирование как есть. Переводи только содержимое."},
                {"role": "user", "content": text},
            ],
            max_tokens=4000,
            temperature=0.1,
        )
        return resp.choices[0].message.content.strip()
    return _gh


def _init_openai():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ImportError("OPENAI_API_KEY не найден в env")
    from openai import OpenAI
    client = OpenAI(api_key=key, timeout=30.0)

    def _oa(text):
        if not text or not text.strip() or len(text) < 3:
            return text
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Переведи следующий текст на русский язык. Сохраняй технические детали, имена переменных, код и форматирование как есть."},
                {"role": "user", "content": text},
            ],
            max_tokens=4000,
            temperature=0.1,
        )
        return resp.choices[0].message.content.strip()
    return _oa


def _init_deepL():
    key = os.environ.get("DEEPL_API_KEY")
    if not key:
        raise ImportError("DEEPL_API_KEY не найден в env")
    import urllib.request
    import urllib.parse
    import json as _json

    def _dl(text):
        if not text or not text.strip() or len(text) < 3:
            return text
        data = urllib.parse.urlencode({
            'auth_key': key,
            'text': text,
            'target_lang': 'RU',
            'source_lang': 'EN',
        }).encode('utf-8')
        req = urllib.request.Request('https://api-free.deepl.com/v2/translate', data=data)
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = _json.loads(resp.read().decode())
        return result['translations'][0]['text']
    return _dl


def _init_argostranslate():
    import argostranslate.package
    import argostranslate.translate

    langs = argostranslate.translate.get_installed_languages()
    if not any(l.code == 'ru' for l in langs) or not any(l.code == 'en' for l in langs):
        raise ImportError("argostranslate: языки en/ru не установлены")

    en = next(l for l in langs if l.code == 'en')
    ru = next(l for l in langs if l.code == 'ru')
    translation = en.get_translation(ru)
    if not translation:
        raise ImportError("argostranslate: перевод не найден")

    def _argos(text):
        if not text or not text.strip() or len(text) < 3:
            return text
        return translation.translate(text)
    return _argos


def _init_deep_translator():
    from deep_translator import GoogleTranslator
    _t = GoogleTranslator(source='auto', target='ru', request_timeout=15)

    def _dt(text):
        try:
            return _t.translate(text)
        except Exception:
            return text
    return _dt


def _init_googletrans():
    from googletrans import Translator
    _t = Translator()

    def _gt(text):
        try:
            return _t.translate(text, dest='ru').text
        except Exception:
            return text
    return _gt


def _init_translatepy():
    from translatepy import Translator as TPT

    def _tp(text):
        try:
            return TPT().translate(text, 'ru').result
        except Exception:
            return text
    return _tp


def _get_translator_unlocked():
"""Возвращает функцию перевода, используя первый работоспособный переводчик.

    Порядок приоритета:
    1. GitHub Models API (GITHUB_TOKEN) — для GitHub Actions
    2. OpenAI API (OPENAI_API_KEY)
    3. DeepL API (DEEPL_API_KEY)
    4. argostranslate (офлайн)
    5. deep_translator (Google Translate, fallback)
    6. googletrans (fallback)
    7. translatepy (fallback)"""
    candidates = [
        ('github-models', _init_github_models),
        ('openai', _init_openai),
        ('deepl', _init_deepL),
        ('argostranslate', _init_argostranslate),
        ('deep_translator', _init_deep_translator),
        ('googletrans', _init_googletrans),
        ('translatepy', _init_translatepy),
    ]

    for name, init_fn in candidates:
        try:
            fn = init_fn()
            test = fn('Hello')
            if test and test not in ('Hello', 'Приветствие'):
                print(f'[переводчик] Использую: {name}', file=sys.stderr)
                return fn
        except Exception as e:
            print(f'[переводчик] {name} недоступен: {e}', file=sys.stderr)
            continue

    print('[переводчик] Ни один переводчик не доступен', file=sys.stderr)

    def _noop(text):
        return text
    return _noop


def get_translator():
    global _translate_fn
    if _translate_fn is None:
        _translate_fn = _get_translator_unlocked()
    return _translate_fn


def init_translator():
    """Принудительно инициализирует переводчик (вызывается при старте)."""
    get_translator()


def is_english(text):
    """Проверяет, содержит ли текст английские буквы."""
    return bool(re.search(r'[A-Za-z]', text))


def get_docstrings(content):
"""Возвращает список (start_line, end_line) для всех docstrings.

    Использует ast для надёжного обнаружения docstrings на уровне модуля,
    классов и функций."""
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return []

    results = []
    nodes_to_check = [tree]
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            nodes_to_check.append(node)

    for n in nodes_to_check:
        if not getattr(n, 'body', None):
            continue
        first = n.body[0]
        if not isinstance(first, ast.Expr):
            continue
        val = first.value
        if isinstance(val, ast.Constant) and isinstance(val.value, str):
            start = first.lineno
            end = getattr(first, 'end_lineno', start)
            results.append((start, end))

    return results


def get_comment_lines(content):
"""Возвращает множество номеров строк, содержащих комментарии.

    Использует tokenize для точного обнаружения комментариев, игнорируя #
    внутри строк."""
    comment_lines = set()
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(content).readline))
        for tok in tokens:
            if tok.type == tokenize.COMMENT:
                comment_lines.add(tok.start[0])
    except (tokenize.TokenError, IndentationError, SyntaxError):
        pass

    return comment_lines


def extract_indent_and_quotes(line):
    """Извлекает отступ и кавычки из строки-начала docstring."""
    stripped = line.lstrip()
    indent = line[:len(line) - len(stripped)]
    quote_match = re.match(r'(?P<q>"""|\'\'\')', stripped)
    if quote_match:
        return indent, quote_match.group('q')
    return indent, '"""'


def translate_docstring_block(content, start, end):
"""Переводит содержимое docstring блока.

    start и end — 1-индексированные номера строк.
    Возвращает новый content с переведённым docstring."""
    lines = content.split('\n')

    indent, quotes = extract_indent_and_quotes(lines[start - 1])

    inner_lines = lines[start - 1:end]
    full_text = '\n'.join(inner_lines)

    inner_match = re.search(
        r'(?P<q>"""|\'\'\')(?P<inner>.*?)(?P=q)',
        full_text,
        re.DOTALL
    )
    if not inner_match:
        return content

    inner = inner_match.group('inner')
    translated = translate_text(inner)

    if translated == inner:
        return content

    new_block = f"{quotes}{translated}{quotes}"
    new_lines = new_block.split('\n')

    lines[start - 1:end] = new_lines
    return '\n'.join(lines)


def translate_docstrings(content):
    """Переводит все docstrings в контентте. Возвращает (new_content, changed)."""
    docstrings = get_docstrings(content)
    changed = False

    for start, end in sorted(docstrings, key=lambda x: x[0], reverse=True):
        lines = content.split('\n')
        inner_lines = lines[start - 1:end]
        full_text = '\n'.join(inner_lines)

        inner_match = re.search(
            r'(?P<q>"""|\'\'\')(?P<inner>.*?)(?P=q)',
            full_text,
            re.DOTALL
        )
        if not inner_match:
            continue

        inner = inner_match.group('inner')
        if not is_english(inner):
            continue

        translated = translate_text(inner)
        if translated != inner:
            content = translate_docstring_block(content, start, end)
            changed = True

    return content, changed


def translate_comments(content):
    """Переводит все комментарии в контентте. Возвращает (new_content, changed)."""
    lines = content.split('\n')
    comment_lines = get_comment_lines(content)
    changed = False

    for i in comment_lines:
        idx = i - 1
        if idx >= len(lines):
            continue
        line = lines[idx]

        match = re.search(r'(?P<code>.*?)(?P<q>""".*?"""|\'\'\'.*?\'\'\'|"[^"]*"|\'[^\']*\')', line)
        hash_pos = line.find('#')

        if hash_pos == -1:
            continue

        before_hash = line[:hash_pos]
        comment_part = line[hash_pos:]

        if not is_english(comment_part):
            continue

        translated = translate_text(comment_part)
        if translated != comment_part:
            lines[idx] = before_hash + translated
            changed = True

    if changed:
        content = '\n'.join(lines)

    return content, changed


def process_file(filepath, dry_run=False):
    """Обрабатывает один Python-файл."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, ds_changed = translate_docstrings(content)
    new_content, cm_changed = translate_comments(new_content)

    if ds_changed or cm_changed:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        print(f"  ИЗМЕНЁН: {filepath}")
        return True
    else:
        print(f"  Пропущен: {filepath}")
        return False


def process_markdown(filepath, dry_run=False):
    """Переводит английский текст в Markdown/RST-файлах на русский."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not is_english(content):
        print(f"  Пропущен (нет английского): {filepath}")
        return False

    lines = content.split('\n')
    code_block = False
    in_code = False
    new_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('```'):
            code_block = not code_block
            new_lines.append(line)
            continue

        if code_block:
            new_lines.append(line)
            continue

        if stripped.startswith('#') or stripped.startswith('*') or stripped.startswith('-'):
            prefix_match = re.match(r'^(\s*[#*\-]\s*)', line)
            if prefix_match:
                prefix = prefix_match.group(1)
                text = line[len(prefix):]
                if is_english(text):
                    translated = translate_text(text)
                    new_lines.append(prefix + translated)
                else:
                    new_lines.append(line)
            else:
                if is_english(stripped):
                    translated = translate_text(line)
                    new_lines.append(translated)
                else:
                    new_lines.append(line)
        else:
            if is_english(stripped) and stripped:
                translated = translate_text(line)
                new_lines.append(translated)
            else:
                new_lines.append(line)

    new_content = '\n'.join(new_lines)
    if new_content != content:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        print(f"  ПЕРЕВЕДЁН: {filepath}")
        return True
    else:
        print(f"  Пропущен: {filepath}")
        return False


def main():
    dry_run = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]

    target = Path(args[0]) if args else Path('.')

    init_translator()

    py_files = []
    md_files = []

    if target.is_file():
        if target.suffix == '.py':
            py_files = [target]
        elif target.suffix in ('.md', '.rst'):
            md_files = [target]
    else:
        py_files = sorted(target.rglob('*.py'))
        md_files = sorted(target.rglob('*.md')) + sorted(target.rglob('*.rst'))

    mode = "DRY RUN" if dry_run else "АКТУАЛЬНЫЙ"
    print(f"Режим: {mode}")
    print(f"Python файлов: {len(py_files)}")
    print(f"Документационных файлов: {len(md_files)}")
    print()

    changed = 0
    for f in py_files:
        print(f"Python: {f}")
        if process_file(f, dry_run):
            changed += 1

    for f in md_files:
        print(f"Документация: {f}")
        if process_markdown(f, dry_run):
            changed += 1

    print(f"\nИзменено файлов: {changed}")
    return changed


if __name__ == '__main__':
    sys.exit(0 if main() >= 0 else 1)
