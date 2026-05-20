# Electronic Health Record Django App

This is a simple Electronic Health Record (EHR) application for students learning Django.

## Features

- Patient CRUD
- Hospital CRUD
- Doctor CRUD
- Registration CRUD
- Django admin model management
- Built-in and custom form validation
- Basic session handling
- Simple REST API using Django REST Framework

## Project Structure

```text
ehr_project/
├── ehr_system/
│   ├── manage.py
│   ├── ehr_system/
│   └── ehr/
│       ├── models.py
│       ├── forms.py
│       ├── views.py
│       ├── services.py
│       ├── serializers.py
│       ├── api_views.py
│       └── templates/ehr/
├── requirements.txt
├── requirement.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv env
env\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
cd ehr_system
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the server:

```bash
python manage.py runserver
```

Open the app:

```text
http://127.0.0.1:8000/
```

Open Django admin:

```text
http://127.0.0.1:8000/admin/
```

## API URLs

- `GET /api/patients/`
- `GET /api/hospitals/`
- `GET /api/doctors/`
- `GET /api/registrations/`

The same API URLs also support `POST`, `PUT`, `PATCH`, and `DELETE`.

## Teaching Notes

This project intentionally uses simple function-based views and plain HTML templates so students can understand the Django request-response flow easily.
