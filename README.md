API-YaTube

API для социальной сети YaTube

Установка:

Клонируйте репозиторий на локальный компьютер

Создайте и активируйте виртуальное окружение

    python3 -m venv venv

    source venv/Scripts/activate
    
Установите зависимости

    pip install -r requirements.txt
    
Выполните миграции

    python manage.py makemigrations

    python manage.py migrate

Пример:

GET: api/v1/posts/ 

Ответ:

    {
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
      {
        "id": 0,
        "author": "string",
        "text": "string",
        "pub_date": "2021-10-14T20:41:29.648Z",
        "image": "string",
        "group": 0
      }
    ]
    }

POST: api/v1/posts/ :

    {
    "text": "string",
    "image": "string",
    "group": 0
    }

Ответ:

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
    }
    
GET: /api/v1/posts/{id}/ :

Ответ:

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
    }
    
PUT: /api/v1/posts/{id}/ :

    {
    "text": "string",
    "image": "string",
    "group": 0
    }
    
Ответ: 

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
    }

PATCH: /api/v1/posts/{id}/ :

    {
    "text": "string",
    "image": "string",
    "group": 0
    }
    
Ответ:

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
    }

DELETE: /api/v1/posts/{id}/ :

Ответ:

    {
    "detail": "Учетные данные не были предоставлены."
    }

GET: /api/v1/posts/{post_id}/comments/ :

Ответ:

    [
    {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
    }
    ]

POST: /api/v1/posts/{post_id}/comments/:

    {
    "text": "string"
    }

Ответ:

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
    }

GET: /api/v1/posts/{post_id}/comments/{id}/ :

Ответ:

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
    }

PUT: /api/v1/posts/{post_id}/comments/{id}/ :

    {
    "text": "string"
    }

Ответ:

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
    }

PATCH: /api/v1/posts/{post_id}/comments/{id}/ :

    {
    "text": "string"
    }

Ответ: 

    {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
    }

DELETE: /api/v1/posts/{post_id}/comments/{id}/ :

Ответ:

    {
    "detail": "Учетные данные не были предоставлены."
    }

GET: /api/v1/groups/ :

Ответ:

    [
    {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
    }
    ]

GET: /api/v1/groups/{id}/ :

Ответ:

    {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
    }

GET: /api/v1/follow/ :

Ответ:

    [
    {
    "user": "string",
    "following": "string"
    }
    ]

POST: /api/v1/follow/ :

    {
    "following": "string"
    }

Ответ:

    {
    "user": "string",
    "following": "string"
    }

POST: /api/v1/jwt/create/:

    {
    "username": "string",
    "password": "string"
    }
   
Ответ: 

    {
    "refresh": "string",
    "access": "string"
    }

POST: /api/v1/jwt/refresh/ :

    {
    "refresh": "string"
    }

Ответ: 

    {
    "access": "string"
    }

POST: /api/v1/jwt/verify/ :

    {
    "token": "string"
    }

Ответ: 

    {
    "token": [
    "Обязательное поле."
    ]
    }
    
Автор: Андрей Алексеевич
