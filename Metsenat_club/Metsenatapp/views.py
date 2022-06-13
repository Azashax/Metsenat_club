from django.shortcuts import render
from rest_framework import status

from .models import *
from .serializers import *
# Create your views here.
from rest_framework.generics import ListCreateAPIView, get_object_or_404, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.aggregates import *


class SponsorListCreateAPIView(ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Sponsor_depositListCreateAPIView(ListCreateAPIView):
    serializer_class = Sponsor_depositSerializer
    queryset = Sponsor_deposit.objects.all()


class Sponsor_depositRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor_deposit.objects.all()
    serializer_class = Sponsor_depositSerializer







class DashboardAPIView(APIView):

    def get(self, request, *args, **kwargs):

        ''' полная сумма спонсоров '''

        all_deposit_sponsor = Sponsor.objects.aggregate(Sum('deposit'))['deposit__sum']
        if all_deposit_sponsor is None:
            all_deposit_sponsor = 0

        ''' сумма кредита студентов '''
        all_deposit_student = Student.objects.aggregate(Sum('deposit_Student'))['deposit_Student__sum']
        if all_deposit_student is None:
            all_deposit_student = 0

        ''' остаток кредита '''
        sum = all_deposit_sponsor + all_deposit_student

        return Response({
            "полная сумма спонсоров": all_deposit_sponsor,
            "сумма кредита студентов": all_deposit_student,
            "остаток кредита": sum,
                         }, status=200)


class StudentDetailView(APIView):
    serializer_class = StudentDeteilSerializer

    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=self.kwargs.get('pk'))
        ''' общая сумма спонсорства'''
        deposit_sum = Student.objects.filter(name=student).aggregate(Sum('sponsor_deposit__deposit'))['sponsor_deposit__deposit__sum']
        if deposit_sum is None:
            deposit_sum = 0

        deposit_sum_cr = student.deposit_Student - deposit_sum
        student.deposit_sum = deposit_sum

        student.deposit_sum_cr = deposit_sum_cr

        serializer = self.serializer_class(instance=student)
        self.update_xa(request)
        return Response(serializer.data, status=200)

    def update_xa(self, request, *args, **kwargs):
        student = get_object_or_404(Student, pk=self.kwargs.get('pk'))

        ''' общая сумма спонсорства'''
        deposit_sum = Student.objects.filter(name=student).aggregate(Sum('sponsor_deposit__deposit'))['sponsor_deposit__deposit__sum']
        if deposit_sum is None:
            deposit_sum = 0

        student.deposit_sum_cr = student.deposit_Student - deposit_sum



    def patch(self, request, pk):
        serializers = StudentDeteilSerializer(self.get(pk), data=request.data)
        if serializers.is_valid():
            serializers.save()
            # self.update_xa(request)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
