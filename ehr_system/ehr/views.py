from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Hospital, Doctor, Registration
from .forms import PatientForm, HospitalForm, DoctorForm, RegistrationForm
from .services import create_registration, get_patient_registration_count


def home(request):
    visit_count = request.session.get('visit_count', 0) + 1
    request.session['visit_count'] = visit_count

    counts = {
        'patient_count': Patient.objects.count(),
        'hospital_count': Hospital.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'registration_count': Registration.objects.count(),
    }

    context = {
        'visit_count': visit_count,
        **counts,
    }
    return render(request, 'ehr/home.html', context)


def clear_session(request):
    request.session.flush()
    return redirect('home')


# Patient CRUD

def patient_list(request):
    request.session['last_section'] = 'Patients'
    patients = Patient.objects.all()
    return render(request, 'ehr/patient_list.html', {'patients': patients})


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'ehr/patient_form.html', {'form': form})


def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    registration_count = get_patient_registration_count(patient)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'ehr/patient_form.html', {
        'form': form,
        'registration_count': registration_count,
    })


def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'ehr/patient_confirm_delete.html', {'patient': patient})


# Hospital CRUD

def hospital_list(request):
    request.session['last_section'] = 'Hospitals'
    hospitals = Hospital.objects.all()
    return render(request, 'ehr/hospital_list.html', {'hospitals': hospitals})


def hospital_create(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()

    return render(request, 'ehr/hospital_form.html', {'form': form})


def hospital_update(request, id):
    hospital = get_object_or_404(Hospital, id=id)

    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)

    return render(request, 'ehr/hospital_form.html', {'form': form})


def hospital_delete(request, id):
    hospital = get_object_or_404(Hospital, id=id)

    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')

    return render(request, 'ehr/hospital_confirm_delete.html', {'hospital': hospital})


# Doctor CRUD

def doctor_list(request):
    request.session['last_section'] = 'Doctors'
    doctors = Doctor.objects.select_related('hospital')
    return render(request, 'ehr/doctor_list.html', {'doctors': doctors})


def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()

    return render(request, 'ehr/doctor_form.html', {'form': form})


def doctor_update(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'ehr/doctor_form.html', {'form': form})


def doctor_delete(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')

    return render(request, 'ehr/doctor_confirm_delete.html', {'doctor': doctor})


# Registration CRUD

def registration_list(request):
    request.session['last_section'] = 'Registrations'
    registrations = Registration.objects.select_related('patient', 'hospital', 'doctor')
    return render(request, 'ehr/registration_list.html', {'registrations': registrations})


def registration_create(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            create_registration(form)
            return redirect('registration_list')
    else:
        form = RegistrationForm()

    return render(request, 'ehr/registration_form.html', {'form': form})


def registration_update(request, id):
    registration = get_object_or_404(Registration, id=id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm(instance=registration)

    return render(request, 'ehr/registration_form.html', {'form': form})


def registration_delete(request, id):
    registration = get_object_or_404(Registration, id=id)

    if request.method == 'POST':
        registration.delete()
        return redirect('registration_list')

    return render(request, 'ehr/registration_confirm_delete.html', {'registration': registration})
