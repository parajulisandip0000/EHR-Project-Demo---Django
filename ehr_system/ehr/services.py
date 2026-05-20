from .models import Doctor, Registration


def get_doctors_for_hospital(hospital):
    return Doctor.objects.filter(hospital=hospital)


def get_patient_registration_count(patient):
    return Registration.objects.filter(patient=patient).count()


def create_registration(form):
    registration = form.save()
    return registration
