from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from .serilizable import PersonSerilizer
from authenticate.models import Register
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

# Create your views here.


# defining the class based view

class PersonList(APIView):
    """
        list all the person and create new person
    """
    
    def get(self, request):
        """ Return all the user data"""
        persons = Person.objects.all()
        serilizer = PersonSerilizer(persons, many=True) 
        return Response(serilizer.data)
    
    
    def post(self, request):
        """ Create a new person instance and save into data base"""
        serilizer = PersonSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            # return Response(serilizer.data, status=status.HTTP_201_CREATED)
            return Response({
                "message": "Person Added Successfully",
                "detail": None,
                "data":serilizer.data
            }, status=status.HTTP_201_CREATED)
        # return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "Error Occured During Person Storing in DB",
            "detail": serilizer.errors,
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)
    

class PersonDetails(APIView):
    """
        Retrieve, update, and delete a Person instance
    """
    
    def get_object(self, pk_id):
        # users = Person.objects.get(pk=pk_id)
        # if users:
        #     return users
        # return NotFound(detail=f"Data not found for Person with id={pk_id}")
        """
        Return the Person instance or None if it doesn't exist.
        """
        qs = Person.objects.filter(pk=pk_id)
        # print("first", qs.values_list('email').first())
        if qs:
            print(qs.values().latest().get('email'))
        return qs.first() if qs.exists() else None 
        
    def get(self, request, pk_id):   
           
        person = self.get_object(pk_id=pk_id)
        
        if person is None:
            return Response({
                "message": "Person not found",
                "detail": None,
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        serilizer = PersonSerilizer(person)
        # return Response(serilizer.data, status=status.HTTP_200_OK)
        return Response({
            "message": "Person fetched successfully",
            "detail": None,
            "data": serilizer.data
        }, status=status.HTTP_200_OK)

    
    def put(self, request, pk_id):
        person = self.get_object(pk_id=pk_id)
        
        if person is None:
            return Response({
                "message": "Person not found, update failed",
                "detail": None,
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)
        
        serilizer = PersonSerilizer(person, data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            # return Response(serilizer.data, status=status.HTTP_200_OK)
            return Response({
                "message": "Data Updated Successfully",
                "detail": None,
                "data": serilizer.data
            }, status=status.HTTP_200_OK)
        # return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "Validation failed",
            "detail": serilizer.errors,
            "data": None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk_id):
        person = self.get_object(pk_id=pk_id)
        
        if person is None:
            return Response({
                "message": "Person not found, delete failed",
                "detail": None,
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)

        
        person.delete()
        return Response({
            "message": "Person deleted successfully",
            "detail": None,
            "data": None
        }, status=status.HTTP_200_OK)