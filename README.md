# test_task
Репозиторий тестового задания

## Запуск приложения
1. Запустить базу командой `docker-compose up -d db`
1. Накатить миграции командой `docker-compose up -d migration`
1. Запустить сервер командой `docker-compose up -d web`
1. Перейти по адресу `localhost:8000`

## Описание
На главной странице реализована форма для загрузки excel файла с расширением `.xlsx`

Для получения отчета следует перейти по адресу `localhost:8000/report`

В поля ввода дат ввести вручную даты в формате `22.08.2023 9:43:50`

После этого уже можно нажать `Получить отчет` и сохранить результат в файл excel.
