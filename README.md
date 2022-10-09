## Установка и запуск
Склонируйте репозиторий в рабочую директорию
 
 `git clone https://github.com/paragonov/nap-api.git`
 
Создайте образы Docker

`docker-compose up -d --build`

### Запуск Telegram-bot

Установите зависимости

`pip install -r requirements.txt`

Перейдите в рабочую директорию бота и запустите файл

`python tg-bot.py`

Зайдите в приложение Telegram и найдите бота @test_news_hack_bot
- команда /start запускает бота

Для остановки приложения используйте

`docker-compose down —volumes`

### Директория analysis предназначена для: 

- предоставления дайджеста новостей
- анализа выборки новостной ленты 
- определения ключевых слов для каждой роли. По ним проводятся ранжирование новостей (частота, расположение), чтобы предоставить самые актуальные новости для выбранной роли.

Назначение каждого файла:
- Analiz.ipynb - файл с анализом
- Words.xlsx и Stop_words.xlsx - ключевые слова 
- data.json - данные, которые получили при парсинге сайтов
