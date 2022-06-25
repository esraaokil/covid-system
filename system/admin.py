from django.contrib import admin
from .models import Profile,Doctor,Patient,Review,ChestDetails,Chronic_diseases,Patient_chronic_diseases,Pregnant_patient,state
# Register your models here.
admin.site.register(state)
admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Review)
admin.site.register(ChestDetails)
admin.site.register(Chronic_diseases)
admin.site.register(Patient_chronic_diseases)
admin.site.register(Pregnant_patient)