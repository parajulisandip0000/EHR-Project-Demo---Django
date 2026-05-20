from django.db import models


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    established_date = models.DateField()

    def __str__(self):
        return self.hospital_name


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor_name


class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return self.patient_name


class Registration(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    symptoms = models.TextField()
    diagnosis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.patient.patient_name