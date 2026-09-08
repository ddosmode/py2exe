# Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

## Проект
Форк [py2exe/py2exe](https://github.com/py2exe/py2exe) на аккаунте `ddosmode`.
Монтирован локально в `/Users/usernarne/Projects/py2exe`.

## Правило перевода документации
**Главное правило для любого fork:** при создании forkа любого кода/приложения необходимо автоматизировать перевод всех docstrings, комментариев и документации на русский язык.

#Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Файл `.github/workflows/translate-to-russian.yml` запускается при каждом пуше на основные ветки. Он:
1. Устанавливает `deep_translator` и `googletrans`.
2. Запускает `scripts/translate_docs.py` для перевода всех `.py`, `.md` и `.rst` файлов.
3. Коммитит переведённые изменения с пометкой `[skip ci]`.

### Килограммовые крючки
Локальная конфигурация hooks находится в `~/.config/kilo/hooks.toml`.
Hook `post-tool-call` (`scripts/translate_docs_hook.py`) автоматически переводит
docstrings и комментарии в изменённых файлах через `scripts/translate_docs.py`.

### Как применить к новому fork
```bash
git clone https://github.com/ddosmode/<repo>.git
cd <repo>
cp -r /Users/usernarne/Projects/py2exe/.github/workflows/translate-to-russian.yml .github/workflows/
cp -r /Users/usernarne/Projects/py2exe/scripts/translate_docs.py .github/scripts/translate_docs.py
git add . && git commit -m "Добавлен workflow для перевода документации на русский" && git push
```

## Структура
```
py2exe/            — основной пакет
tests/             — тесты
docs/              — документация
.github/workflows/ — CI и перевод
scripts/           — вспомогательные скрипты
```

## Команды
```bash
python -m pytest tests/    — запуск тестов
python scripts/translate_docs.py . — перевод docstrings и комментариев
```
