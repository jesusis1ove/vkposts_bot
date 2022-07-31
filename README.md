## vkposts bot
tg.me/oneplacemarket 

Забирает публикации из сообществ vk.com в телеграм канал по заданному шаблону
### Requirements
* Python 3
* vk-api 11.9.8
* pyTelegramBotAPI 4.1.1
* requests

### Установка
Установка и создание виртуального окружения
```
git clone https://github.com/jesusis1ove/vkposts_bot
python3 -m venv venv
venv\Scripts\activate
```
Установка зависимостей
```
pip install --upgrade
pip install -r requirements.txt
```
### Настройка
Настраиваем config.py: 

```TG_TOKEN``` - ..\
```CHANNEL_ID``` - ..\
```VK_ACCESS_TOKEN``` - ..\
```POST_HTML_TEMPLATE``` - ..\
```TAGS``` -

### Запуск
```
python3 main.py
```
