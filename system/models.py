import profile
from django.db import models
from django.conf import settings
from PIL import Image
import os
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import django.utils.datetime_safe
import datetime
from django.utils.translation import gettext as _

# Create your models here.

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

 
class state(models.Model):
    state_arabic=models.CharField(_("governorate_name_ar"),max_length=50)  
    state_english=models.CharField(_("governorate_name_en"),max_length=50)   

          

class Profile(models.Model):
    type_choices= (
        ('doctor','doctor'),
        ('patient','patient')
    )

    six=(
        ('male','male'),
        ('famale','famale')
    )
    type_name=models.CharField(max_length=50, blank=True,null=True,  choices=type_choices)
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=500, blank=True,null=True )
    password = models.CharField(max_length=200, blank=True,null=True)
    gander= models.CharField(max_length=50, blank=True,null=True, choices=six)
    #city = models.CharField(max_length=200, blank=True, )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,  blank=True,null=True, unique=True) # Validators should be a list
    #created = models.DateTimeField(default=datetime(2017, 7, 28, 7, 58, 21))
    profile_image=models.ImageField(upload_to=upload_to, blank=True, null=True)
    #type_id=models.OneToOneField(Type, related_name='type_profile', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=['name']   
    
    
class Doctor(Profile):
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    national_id=models.IntegerField(blank=True, null=True)
    identification=models.ImageField(upload_to=upload_to, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    doctor_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    #profile_id=models.ForeignKey(Profile, related_name='doctor_profile', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=['name']  

class Patient(Profile):
    patientDoctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_patient_set')
    patient_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    #profile_id=models.ForeignKey(Profile, related_name='patient_profile', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    
class Review(models.Model):
    # The first element in each tuple is the actual value to be set on the model,
    # and the second one is the human-readable name.
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True,related_name='review')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='review') 
    review_comment = models.TextField(null=True, blank=True)
    evaluation = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    
    class Meta:
        # a user can leave only one review to each doctor
        # so we can never have more than one review with the same patient on the same doctor's profile in the database
        unique_together = [['owner', 'doctor']]

    def __str__(self):
        return self.evaluation

class ChestDetails(models.Model):
    COVID_RESULT = (
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    )
    # owner = models.ForeignKey(
    #     Patient, on_delete=models.CASCADE, null=True, blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=True)
    x_ray_image=models.ImageField(upload_to=upload_to, blank=True, null=True)
    status = models.CharField(max_length=10, choices=COVID_RESULT) # boolean
    regestration_date = models.DateTimeField(auto_now_add=True)
    patient_id=models.ForeignKey(Patient, related_name='patient_x_ray', on_delete=models.CASCADE,null=True, blank=True)
    
    # TO-DO
    # live_location = models.CharField(max_length=200, blank=True, null=True) #

    def __str__(self):
        return str(self.status)

class Chronic_diseases(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=True)
    diseases_name=models.CharField(max_length=200, blank=True, null=True)

class Patient_chronic_diseases(models.Model):
    
    chronic_diseases_id=models.ForeignKey(Chronic_diseases,related_name='diseases', on_delete=models.CASCADE,null=True, blank=True) 
    patient_id=models.ForeignKey(Patient,related_name='diseases', on_delete=models.CASCADE,null=True, blank=True)                                         

class Pregnant_patient(models.Model): 
     pregnancy_month =models.IntegerField(blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     patient_id=models.ForeignKey(Patient,related_name='Pregnant', on_delete=models.CASCADE,null=True, blank=True)

     