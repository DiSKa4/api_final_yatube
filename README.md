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

GET: api/v1/posts/ Ответ:

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
    
Автор: Андрей Алексеевич
