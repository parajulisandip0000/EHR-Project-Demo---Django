from rest_framework import serializers
from .models import Patient, Hospital, Doctor, Registration


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

    def validate(self, data):
        hospital = data.get('hospital')
        doctor = data.get('doctor')

        if hospital and doctor and doctor.hospital != hospital:
            raise serializers.ValidationError('Selected doctor must work in the selected hospital.')

        return data
