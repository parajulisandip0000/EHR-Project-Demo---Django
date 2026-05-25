# Electronic Health Record System

A Django-based Electronic Health Record (EHR) project for managing hospitals, doctors, patients, and patient registrations. The application provides basic CRUD screens, a dashboard with record counts, validation rules, and simple service logic for patient categories, emergency detection, and doctor registration limits.

## Features

- Dashboard showing total patients, hospitals, doctors, and registrations.
- Patient management: create, view, update, and delete patient records.
- Hospital management: create, view, update, and delete hospital records.
- Doctor management: create, view, update, and delete doctor records.
- Registration management: assign patients to hospitals and doctors.
- Django admin support for all main models.
- Form validation for age, phone numbers, and doctor/hospital matching.
- Automatic patient category display:
  - `Minor` for patients under 18.
  - `Adult` for patients 18 or older.
- Emergency flagging when registration symptoms contain the word `heart`.
- Doctor capacity check that prevents more than 20 registrations per doctor.

## Project Structure

```text
ehr_project/
|-- README.md
|-- requirements.txt
|-- ehr_system/
|   |-- manage.py
|   |-- ehr_system/
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- asgi.py
|   |   `-- wsgi.py
|   `-- ehr/
|       |-- admin.py
|       |-- apps.py
|       |-- forms.py
|       |-- models.py
|       |-- services.py
|       |-- urls.py
|       |-- views.py
|       |-- migrations/
|       |-- static/
|       |   `-- ehr/
|       |       `-- style.css
|       `-- templates/
|           `-- ehr/
`-- env/
```

## Requirements

- Python 3.12 or newer
- pip
- Virtual environment support
- Django 6.0.5, installed from `requirements.txt`

## Setup Instructions

### 1. Open the Project Folder

```powershell
cd "D:\Study\KU HI151\ehr_project"
```

### 2. Create a Virtual Environment

If the `env` folder already exists, you can skip this step.

```powershell
python -m venv env
```

### 3. Activate the Virtual Environment

```powershell
.\env\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again.

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 5. Move Into the Django Project Directory

```powershell
cd ehr_system
```

### 6. Apply Database Migrations

```powershell
python manage.py migrate
```

This creates the SQLite database file at:

```text
ehr_system/db.sqlite3
```

### 7. Create an Admin User

```powershell
python manage.py createsuperuser
```

Follow the prompts to enter a username, email address, and password.

### 8. Run the Development Server

```powershell
python manage.py runserver
```

Open the application in a browser:

```text
http://127.0.0.1:8000/
```

Open the Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

## Main Application Pages

| Page | URL |
| --- | --- |
| Dashboard | `/` |
| Patient list | `/patients/` |
| Add patient | `/patients/create/` |
| Hospital list | `/hospitals/` |
| Add hospital | `/hospitals/create/` |
| Doctor list | `/doctors/` |
| Add doctor | `/doctors/create/` |
| Registration list | `/registrations/` |
| Add registration | `/registrations/create/` |
| Django admin | `/admin/` |

## Data Models

### Hospital

Stores hospital details:

- Hospital name
- Address
- Phone
- Email
- Established date

### Doctor

Stores doctor details:

- Doctor name
- Specialization
- Phone
- Email
- Hospital

Each doctor belongs to one hospital.

### Patient

Stores patient details:

- Patient name
- Age
- Gender
- Address
- Phone
- Blood group

### Registration

Stores a patient registration:

- Patient
- Hospital
- Doctor
- Registration date
- Symptoms
- Diagnosis

The registration date is created automatically.

## Important Business Rules

### Patient Category

Patient category is calculated in `ehr/services.py`:

- Age below 18: `Minor`
- Age 18 or above: `Adult`

### Emergency Case Detection

A registration is marked as an emergency case when the symptoms text contains:

```text
heart
```

Example symptoms that trigger emergency detection:

```text
heart pain
severe heart problem
fast heartbeat
```

### Doctor Registration Limit

A doctor can have a maximum of 20 registrations. If a doctor already has 20 or more registrations, the system prevents creating another registration for that doctor.

### Doctor and Hospital Matching

When creating or updating a registration, the selected doctor must belong to the selected hospital. If the doctor works at a different hospital, the form shows a validation error.

### Form Validation

The system validates:

- Patient age must be greater than 0.
- Phone numbers can contain only digits, spaces, `+`, and `-`.
- Hospital and doctor must match during registration.

## Recommended Data Entry Order

Use this order when adding sample data:

1. Add one or more hospitals.
2. Add doctors and assign each doctor to a hospital.
3. Add patients.
4. Create registrations by selecting a patient, hospital, and matching doctor.

## Common Commands

Run these commands from the `ehr_system` directory.

### Start Server

```powershell
python manage.py runserver
```

### Create Migrations After Model Changes

```powershell
python manage.py makemigrations
```

### Apply Migrations

```powershell
python manage.py migrate
```

### Create Admin User

```powershell
python manage.py createsuperuser
```

### Check Project Configuration

```powershell
python manage.py check
```

### Open Django Shell

```powershell
python manage.py shell
```

## Static Files

The main stylesheet is located at:

```text
ehr_system/ehr/static/ehr/style.css
```

Templates load this stylesheet using Django's static file system.

## Templates

HTML templates are located at:

```text
ehr_system/ehr/templates/ehr/
```

The project includes separate templates for list, form, and delete-confirmation pages for each main entity.

## Admin Panel

All main models are registered in `ehr/admin.py`:

- Hospital
- Doctor
- Patient
- Registration

After creating a superuser, visit:

```text
http://127.0.0.1:8000/admin/
```

## Troubleshooting

### `python` Is Not Recognized

Install Python and make sure it is added to your system `PATH`. On Windows, you may also try:

```powershell
py --version
```

If `py` works, use:

```powershell
py manage.py runserver
```

### Virtual Environment Will Not Activate

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then run:

```powershell
.\env\Scripts\Activate.ps1
```

### Database Table Does Not Exist

Run migrations:

```powershell
python manage.py migrate
```

### Port 8000 Is Already in Use

Run the server on a different port:

```powershell
python manage.py runserver 8001
```

Then open:

```text
http://127.0.0.1:8001/
```

### Doctor Does Not Appear Valid During Registration

Make sure the doctor is assigned to the same hospital selected in the registration form.

## Development Notes

- This project uses SQLite for local development.
- `DEBUG` is currently enabled in `settings.py`.
- `ALLOWED_HOSTS` is empty, which is acceptable for local development but must be configured before deployment.
- The `SECRET_KEY` is stored directly in `settings.py`; move it to an environment variable before production use.
- This project is intended for learning and local demonstration, not direct production use without security and privacy improvements.

## Production Considerations

Before deploying a real EHR system, update the project to include:

- Secure environment-based configuration.
- Strong authentication and role-based access control.
- HTTPS-only deployment.
- Audit logs for patient record access and changes.
- Encrypted backups.
- Proper patient privacy and healthcare compliance review.
- A production database such as PostgreSQL.
- Static file collection and serving through a production-ready web server.
