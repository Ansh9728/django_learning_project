from .models import Person
from rest_framework import serializers


class PersonSerilizer(serializers.Serializer):
    """
        Serializer for the Person model, handling validation and serialization of person-related data.
    """
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField(required=True)
    address = serializers.CharField(max_length=255, required=False)
    phone_number = serializers.CharField(required=False)
    date_of_birth = serializers.DateField()
    
    
    def create(self, validated_data):
        """
            create and return a new instance of the the person data
        """
        return Person.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
            update and return the existing person instance given the validated data
        """ 
        
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        
        return instance