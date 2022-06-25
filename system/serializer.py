import imp
from rest_framework import serializers
from system.models import Profile,Doctor,Patient,Review,ChestDetails,Chronic_diseases,Patient_chronic_diseases,Pregnant_patient,state


class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model=state
        fields=['state_arabic','state_english'] 
 
class ProfileSerializer(serializers.ModelSerializer):
    profile_image= serializers.ImageField(required=False)

    class Meta:
        model=Profile
        fields='__all__'
        #fields= ('name','email','password','gander','city','phone_number','profile_image','type_id')


class DoctorSerializer(serializers.ModelSerializer):
    identification= serializers.ImageField(required=False)

    class Meta:
        model=Doctor
        fields=['short_intro','bio','national_id','identification','social_website','doctor_patient_set','review']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['patient_x_ray',' patientDoctor','patient_id','profile_id','diseases','Pregnant']

class ChestDetailsSerializer(serializers.ModelSerializer):
    x_ray_image= serializers.ImageField(required=False)

    class Meta:
        model=ChestDetails
        fields='__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'


class Chronic_diseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chronic_diseases
        fields='__all__'


class Patient_chronic_diseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient_chronic_diseases
        fields='__all__'


class Pregnant_patientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pregnant_patient
        fields='__all__'

