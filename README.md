# my-fastapi-template

**Database:** asyncpg, alembic, sqlalchemy

**Creator:** [@begenFys](https://t.me/begenFys)

**Creator's channel:** [@begenFys_life](https://t.me/begenFys_life)

[Source](https://github.com/zhanymkanov/fastapi-best-practices#1-project-structure-consistent--predictable)

## Настройка окружения
1. Установка виртуального окружения и зависимостей
```shell
pip install pipenv

pipenv shell

pipenv sync
```

2. Заполнить env файл

3. Накатить миграции
```shell
alembic upgrade head
```

## Запуск проекта
1. Запускаем тестовый шаблон
```shell
uvicorn src.api.main:app --reload
```

## Запуск через Docker

## Запуск через Docker-Compose