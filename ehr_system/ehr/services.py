from .models import Doctor, Registration


def patient_category(age):
    if age < 18:
        return "Minor"

    return "Adult"


def emergency_case(symptoms):
    if "heart" in symptoms.lower():
        return True

    return False


def doctor_limit(doctor):
    total = Registration.objects.filter(doctor=doctor).count()

    if total >= 20:
        return False

    return True


def get_doctors_for_hospital(hospital):
    return Doctor.objects.filter(hospital=hospital)


def get_patient_registration_count(patient):
    return Registration.objects.filter(patient=patient).count()


def create_registration(form):
    registration = form.save()
    return registration
