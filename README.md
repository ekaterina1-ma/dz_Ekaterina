# dz_Ekaterina

## Запуск автотестов

1. Установить зависимости:
   pip install -r requests

2. Задать переменную окружения:
   YOUGILE_TOKEN — API токен Yougile

   macOS / Linux:
   export YOUGILE_TOKEN=your_token

   Windows (PowerShell):
   setx YOUGILE_TOKEN "your_token"

3. Запустить тесты:
   pytest 08_lesson
