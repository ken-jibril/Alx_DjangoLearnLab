# Social Media API

## Setup

1. Clone repository
2. Create virtual environment
3. Install dependencies:
   pip install django djangorestframework
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Start server:
   python manage.py runserver

## Endpoints
```
- POST /api/register/ → Register new user

- POST /api/login/ → Login user

- GET /api/profile/ → Retrieve logged-in user profile (Token required)
```

## Authentication

Token-based authentication using Django REST Framework.
Each successful registration/login returns a token.