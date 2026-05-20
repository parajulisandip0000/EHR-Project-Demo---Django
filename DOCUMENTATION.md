# EHR Application Documentation

## 1. Models

The app has four main models:

- `Patient`: stores patient information such as name, age, gender, phone, and blood group.
- `Hospital`: stores hospital name, address, phone, email, and established date.
- `Doctor`: stores doctor details and connects each doctor to one hospital.
- `Registration`: connects patient, hospital, and doctor for a hospital visit.

These models are registered in `ehr/admin.py`, so they can be managed from Django Administration.

## 2. Views and Templates

Each model has simple CRUD pages:

- Create a record
- Display records in a table
- Update a record
- Delete a record

Example:

- `/patients/`
- `/hospitals/`
- `/doctors/`
- `/registrations/`

## 3. Form Validation

Validation is written in `ehr/forms.py`.

Examples:

- Patient age must be greater than `0`.
- Phone numbers should contain digits only.
- During registration, the selected doctor must belong to the selected hospital.

Django automatically displays form errors when `{{ form.as_p }}` is used in the template.

## 4. Services

Custom business logic is placed in `ehr/services.py`.

Examples:

- Count how many registrations a patient has.
- Create a registration through a service function.
- Get doctors for a selected hospital.

Keeping this logic in services makes views easier to read.

## 5. Session Handling

The app uses Django's built-in session framework.

Examples:

- Home page visit count is stored in session.
- The last opened section is stored in session.
- Session data can be cleared from the home page.

## 6. API Development

The API uses Django REST Framework.

Important files:

- `ehr/serializers.py`: converts model data to JSON and JSON to model data.
- `ehr/api_views.py`: provides CRUD API logic.
- `ehr/urls.py`: registers API routes.

Example API endpoints:

- `/api/patients/`
- `/api/hospitals/`
- `/api/doctors/`
- `/api/registrations/`

## 7. Basic Workflow

1. Create hospital records first.
2. Create doctor records and assign doctors to hospitals.
3. Create patient records.
4. Create registration records by selecting patient, hospital, and doctor.
