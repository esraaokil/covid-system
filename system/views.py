from django.shortcuts import render
from .models import Profile,Doctor,Patient,Review,ChestDetails,Chronic_diseases,Patient_chronic_diseases,Pregnant_patient,state
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import  ProfileSerializer,DoctorSerializer,PatientSerializer,ChestDetailsSerializer,ReviewSerializer,Chronic_diseasesSerializer,Patient_chronic_diseasesSerializer,Pregnant_patientSerializer,stateSerializer
from rest_framework import status, filters

# Create your views here.

@api_view(['GET'])
def state_create(request):
    # GET
    if request.method == 'GET':
        s = state.objects.all()
        serializer = stateSerializer(s, many=True)
        return Response(serializer.data)

#profile 
@api_view(['GET','POST'])
def profile_create(request):
    # GET
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ProfileSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def profile_edit(request,  pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
        
    #PUT
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        profile.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


#doctor
@api_view(['GET','POST'])
def doctor_create(request):
    # GET
    if request.method == 'GET':
        doctor = Doctor.objects.all()
        serializer =DoctorSerializer(doctor, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = DoctorSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def doctor_edit(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        doctor.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


#Patient
@api_view(['GET','POST'])
def patient_create(request):
    # GET
    if request.method == 'GET':
        patient = Patient.objects.all()
        serializer =PatientSerializer(patient, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = PatientSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def patient_edit(request, pk):

    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        patient.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#chestDetails
@api_view(['GET','POST'])
def chest_create(request):
    # GET
    if request.method == 'GET':
        chest = ChestDetails.objects.all()
        serializer =ChestDetailsSerializer(chest, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ChestDetailsSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def chest_edit(request, pk):
    try:
        chest = ChestDetails.objects.get(pk=pk)
    except ChestDetails.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ChestDetailsSerializer(chest)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = ChestDetailsSerializer(chest, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        chest.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#review      
@api_view(['GET','POST'])
def review_create(request):
    # GET
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ReviewSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def review_edit(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
        
    #PUT
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        review.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


#Chronic_diseases
@api_view(['GET','POST'])
def diseases_create(request):
    # GET
    if request.method == 'GET':
        diseases = Chronic_diseases.objects.all()
        serializer = Chronic_diseasesSerializer(diseases, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = Chronic_diseasesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def diseases_edit(request, pk):
    try:
        diseases = Chronic_diseases.objects.get(pk=pk)
    except Chronic_diseases.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = Chronic_diseasesSerializer(diseases)
        return Response(serializer.data)
        
    #PUT
    elif request.method == 'PUT':
        serializer = Chronic_diseasesSerializer(diseases, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        diseases.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


#Patient_chronic_diseases
@api_view(['GET','POST'])
def patient_diseases_create(request):
    # GET
    if request.method == 'GET':
        patient_diseases = Profile.objects.all()
        serializer = Patient_chronic_diseasesSerializer(patient_diseases, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = Patient_chronic_diseasesSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def patient_diseases_edit(request, pk):
    try:
        patient_diseases = Patient_chronic_diseases.objects.get(pk=pk)
    except Patient_chronic_diseases.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = Patient_chronic_diseasesSerializer(patient_diseases)
        return Response(serializer.data)
        
    #PUT
    elif request.method == 'PUT':
        serializer = Patient_chronic_diseasesSerializer(patient_diseases, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        patient_diseases.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
  
#pregnant_patient
@api_view(['GET','POST'])
def pregnant_create(request):
    # GET
    if request.method == 'GET':
        pregnant = Pregnant_patient.objects.all()
        serializer = Pregnant_patientSerializer(pregnant, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = Pregnant_patientSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def pregnant_edit(request, pk):
    try:
        pregnant = Pregnant_patient.objects.get(pk=pk)
    except Pregnant_patient.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = Pregnant_patientSerializer(pregnant)
        return Response(serializer.data)
        
    #PUT
    elif request.method == 'PUT':
        serializer = Pregnant_patientSerializer(pregnant, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        pregnant.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)