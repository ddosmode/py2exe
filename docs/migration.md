Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
===================

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

#Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
|-----------------------------|----------------------------------------------------|------------------------------------------|
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
| Информация о версии Pass | Н/Д | Используйте аргумент `version_info` |
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

#Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

## Оператор импорта

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

## Переносим вызов функции

Несколько подробностей о том, как перейти от вызова `setup` к `freeze`:

- Аргументы «console», «windows», «service», «data_files» и «zipfile» можно использовать с «freeze», как и в «setup».
- Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
- Словарь `option` также можно использовать повторно, но мы рекомендуем отказаться от дополнительного ключа `py2exe`, так как его поддержка будет прекращена в будущем.
- Параметры «includes», «excludes», «packages» и «dll_excludes» теперь должны представлять собой списки, а не строки, разделенные запятыми. Текущий синтаксис по-прежнему поддерживается, но в будущем он будет удален.
- Словарь `version_info` поддерживает запись некоторой информации в свойствах замороженного исполняемого файла. Эта функция, несмотря на рекламу, не работала со старыми версиями py2exe. Если вы собираетесь использовать эту функцию, преобразуйте сценарий заморозки в новый API.
- Все остальные аргументы, специфичные для distutils, включая, помимо прочего, `name`, `author`, `version`, `url` и т. д., не поддерживаются `freeze` и при их передаче вызывают `TypeError`. Пожалуйста, удалите эти дополнительные аргументы из вызова «freeze», поскольку «py2exe» не предназначен для их использования.
