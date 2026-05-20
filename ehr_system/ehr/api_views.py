from rest_framework import viewsets
from .models import Patient, Hospital, Doctor, Registration
from .serializers import (
    PatientSerializer,
    HospitalSerializer,
    DoctorSerializer,
    RegistrationSerializer,
)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.select_related('hospital')
    serializer_class = DoctorSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.select_related('patient', 'hospital', 'doctor')
    serializer_class = RegistrationSerializer
