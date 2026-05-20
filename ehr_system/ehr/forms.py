from django import forms
from .models import Patient, Hospital, Doctor, Registration


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <= 0:
            raise forms.ValidationError('Age must be greater than 0.')
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number should contain digits only.')
        return phone


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'
        widgets = {
            'established_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number should contain digits only.')
        return phone


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number should contain digits only.')
        return phone


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        hospital = cleaned_data.get('hospital')
        doctor = cleaned_data.get('doctor')

        if hospital and doctor and doctor.hospital != hospital:
            raise forms.ValidationError('Selected doctor must work in the selected hospital.')

        return cleaned_data
