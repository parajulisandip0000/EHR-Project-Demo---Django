from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/update/<int:id>/', views.patient_update, name='patient_update'),
    path('patients/delete/<int:id>/', views.patient_delete, name='patient_delete'),

    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('hospitals/create/', views.hospital_create, name='hospital_create'),
    path('hospitals/update/<int:id>/', views.hospital_update, name='hospital_update'),
    path('hospitals/delete/<int:id>/', views.hospital_delete, name='hospital_delete'),

    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('doctors/update/<int:id>/', views.doctor_update, name='doctor_update'),
    path('doctors/delete/<int:id>/', views.doctor_delete, name='doctor_delete'),

    path('registrations/', views.registration_list, name='registration_list'),
    path('registrations/create/', views.registration_create, name='registration_create'),
    path('registrations/update/<int:id>/', views.registration_update, name='registration_update'),
    path('registrations/delete/<int:id>/', views.registration_delete, name='registration_delete'),
]
