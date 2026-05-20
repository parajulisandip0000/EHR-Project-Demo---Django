from django.contrib import admin
from .models import Hospital, Doctor, Patient, Registration

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Registration)