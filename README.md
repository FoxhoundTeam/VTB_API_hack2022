[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub contributors](https://img.shields.io/github/contributors/Ornstein89/VTB_API_hack2022)

# VTB_API_hack2022

# Инструкция по запуску
Демо решение расположено по адресу [http://51.250.82.157/](51.250.82.157)

Логин: admin@example.com
Пароль: 1234

Для запуска локально, см. [Развертывание через docker-compose](#развертывание-через-docker-compose)

# Развертывание через docker-compose
1. Установить [docker](https://docs.docker.com/engine/install/ubuntu/)
2. В папке compose создать файл .env и [заполнить](#описание-переменных-окружения) его в соответствии с примерами
3. Запустить команду docker compose up -d с правами суперпользователя
```bash
sudo docker compose up -d
```
5. Настроить внешний nginx, который будет пересылать все запросы на порт приложения

# Описание переменных окружения

## HTTP_PORT
Файлы: .env

Тип: целое число

Назначение: порт на котором будет крутиться приложение

## MONGODB_SERVER
Файлы: .env

Тип: строка

Назначение: хост mongodb (обычно указывается как db)

## RMQ_HOST
Файлы: .env

Тип: строка

Назначение: хост rabbitmq

## RMQ_PORT
Файлы: .env

Тип: строка

Назначение: порт rabbitmq (по умолчанию 5672)
## RMQ_USER
Файлы: .env

Тип: строка

Назначение: пользователь rabbitmq
## RMQ_PASS
Файлы: .env

Тип: строка

Назначение: пароль rabbitmq

## JWT_SECRET
Файлы: .env

Тип: строка

Назначение: секретное значение для генерации JWT токенов

# Команды docker-compose 
Все команды необходимо выполнять в папке compose
- Остановить все контейнеры
```bash
sudo docker-compose stop
```
- Перезапустить контейнер
```bash
sudo docker-compose restart {container_name}
```
- Запуск ipython
```bash
sudo docker-compose exec backend ipython
```

