from django.contrib import admin
from .models import Doctor,Speciality,Appointment,Bill,Reciept,Report,DetailsofPatient,Prescription
admin.site.register(Doctor)
admin.site.register(Speciality)
admin.site.register(Appointment)
admin.site.register(Bill)
admin.site.register(Reciept)
admin.site.register(Report)
admin.site.register(DetailsofPatient)
admin.site.register(Prescription)
# Register your models here.
