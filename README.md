# Инстаграм бот

Проект создан для управлением аккаунтом инстаграма

## Предварительные условия:

Для запуска у вас уже должен быть установлен  python 3

## Установка:

Пункт 1: Зайдите в командную строку 

Введите в поисковике 'Командная строка'

```bash
```
Пункт 2: Перейдите в папку с кодом в командной строке

```bash
$ cd ..\api 4 урок
$ C:\api 4 урок>
```

Пункт 3: Установите зависимости

```bash
$ pip install -r requirements.txt
```
Пункт 4: запишите свой логин и пароль к инстаграмму

можно записать прям в коде 

```bash
bot = Bot(like_delay=60)
bot.login(username= username , password=password)
```
или для безопасности создать фаил .env

```bash
.env
INSTAGRAM_USERNAME=username
INSTAGRAM_PASSWORD=password
```

```bash
py.py
bot = Bot(like_delay=60)
bot.login(username=instagram_username, password=instagram_password)
```
