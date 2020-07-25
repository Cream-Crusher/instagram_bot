# Инстаграм бот

Проект создан для управлением аккаунтом инстаграма, а в частности залив фото

## Предварительные условия:

Для запуска у вас уже должен быть установлен  python 3

## Установка:

Пункт 1: Зайдите в командную строку 

Введите в поисковике 'Командная строка'

```bash
```
Пункт 2: Перейдите в папку с кодом в командной строке

```bash
$ cd ..\instagram_bot
$ C:\instagram_bot>
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

.env
```bash
INSTAGRAM_USERNAME=username
INSTAGRAM_PASSWORD=password
```

py.py
```bash
bot = Bot(like_delay=60)
bot.login(username=instagram_username, password=instagram_password)
```

Пункт 5: запустите код

```bash
$ py.py
```

Пункт 6: выберите действие

```bash
Which account do you want to use? (Type number)
$ 1: 'login'
$ 0: add another account.
$ -1: delete all accounts.
```

###Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
