from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['gender', 'first_name','last_name', 
                    'dob_month', 'dob_day', 'dob_year',
                    'height', 'weight']

