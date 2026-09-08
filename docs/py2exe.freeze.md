<!-- markdownlint-disable -->

# <kbd>функция</kbd> `freeze`

```python
freeze(
    console=[],
    windows=[],
    service=[],
    data_files=None,
    zipfile='library.zip',
    options={},
    version_info={}
)
```

Создайте замороженный исполняемый файл из переданных скриптов Python.



**Аргументы:**
 
 - <b>`console`</b> (список dict): пути к файлам Python, которые будут заморожены как исполняемые файлы консоли (CLI). См. ниже синтаксис целевого dict.
 - <b>`windows`</b> (список dict): пути к файлам Python, которые будут заморожены как исполняемые файлы Windows (GUI). См. ниже синтаксис целевого dict.
 - <b>`service`</b> (список dict): имена модулей и параметры для исполняемых файлов службы Windows. См. ниже синтаксис целевого dict.
 - <b>`data_files`</b> (список): файлы, отличные от Python, которые необходимо добавить в замороженный пакет. Каждый элемент списка представляет собой кортеж, содержащий путь назначения в пакете и исходный путь к файлам данных.
 - <b>`zipfile`</b> (str): целевой путь к архиву, который будет содержать все пакеты и модули Python, необходимые для замороженного пакета.  Если для этого параметра установлено значение «Нет», архив будет прикреплен к целевому исполняемому файлу.
 - <b>`options`</b> (dict): параметры, используемые для настройки и настройки пакета.  Поддерживаемые значения перечислены ниже.
 - <b>`version_info`</b> (dict): строки версии и другую информацию можно прикрепить к исполняемому файлу Windows, настроив этот словарь.  Поддерживаемые значения перечислены ниже.

Целевые словари (для использования в консоли или Windows):
 - <b>`script`</b> (str): путь к модулю Python целевого исполняемого файла.
 - <b>`dest_base`</b> (str): необязательно, каталог и базовое имя исполняемого файла.  Если каталог содержится, он должен быть одинаковым для всех целей.
 - <b>`bitmap_resources`</b> (список): список кортежей из двух `(id, путь)`.  Растровые файлы добавлены в комплект.
 - <b>`icon_resources`</b> (список): список из двух кортежей `(id, путь)` Значок, используемый для исполняемого файла.
 - <b>`other_resources`</b> (список): список из трёх кортежей `(resource_type, id, datastring)` Другие файлы, добавленные в пакет.
 - <b>`version_info`</b> (dict): дополнительно указывает информацию о версии для данного двоичного файла.  Поддерживаемые значения перечислены ниже.

Целевые словари (будут использоваться для «сервиса»):
 - <b>`modules`</b> (список или строка): одно или несколько имен модулей Python, которые предоставляют классы обслуживания (классы с `_svc_name_`).
 - <b>`cmdline_style`</b> (str): поведение службы в командной строке. Поддерживаемые значения: py2exe (по умолчанию; устаревшая обработка команд установки и удаления в стиле py2exe), pywin32 (использует win32serviceutil.HandleCommandLine; один класс службы) и custom (вызывает HandleCommandLine() на уровне модуля; один служебный модуль).
 - <b>`other_target_keys`</b> (примечание): то же, что и цели `console`/`windows` (например, `dest_base`, `icon_resources`, `other_resources`, `version_info`).

Опции («опции»):
 - <b>`includes`</b> (список): список модулей, которые нужно включить в комплект.
 - <b>`excludes`</b> (список): список модулей, которые нужно исключить из пакета.
 - <b>`packages`</b> (список): список пакетов, которые нужно включить в комплект. Примечание: этот параметр НЕ является рекурсивным. Будут включены только модули первого уровня пакета.
 - <b>`dll_excludes`</b> (список): список DLL, которые нужно исключить из пакета.
 - <b>`dist_dir`</b> (str): целевой путь к пакету, по умолчанию `dist`.
 - <b>`compressed`</b> (int): если `1`, создать сжатый архив целевой библиотеки.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - <b>`optimize`</b> (int): уровень оптимизации файлов Python, встроенных в пакет.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Уровни файлов пакетов (`bundle_files`): среда выполнения py2exe *может* использовать модуль расширения, напрямую импортируя их из zip-архива - без необходимости распаковывать их в файловую систему. Параметр Bundle_files указывает, куда помещаются модули расширения, сама библиотека Python и другие необходимые библиотеки DLL.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

*Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.


 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
 - Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.


---

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
