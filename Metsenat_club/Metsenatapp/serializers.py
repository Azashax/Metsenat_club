from .models import *
from rest_framework import serializers


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentDeteilSerializer(serializers.ModelSerializer):
    deposit_sum = serializers.IntegerField()
    deposit_sum_cr = serializers.IntegerField()
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1


class Sponsor_depositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor_deposit
        fields = '__all__'