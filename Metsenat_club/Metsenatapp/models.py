from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

TYPE = (
    ("Undergraduate", "Undergraduate"),
    ("Magistracy", "Magistracy")
)


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=128, null=True, blank=True)
    numbers = models.CharField(max_length=128, null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sponsor_name

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'


class Sponsor_deposit(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)


    class Meta:
        verbose_name = 'Sponsor_deposit'
        verbose_name_plural = 'Sponsor_deposit'


class Institute_name(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Institute_name'
        verbose_name_plural = 'Institute_name_s'


class Student(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    numbers = models.CharField(max_length=128, null=True, blank=True)
    deposit_Student = models.IntegerField(default=1300, null=True, blank=True, validators=[
        MinValueValidator(limit_value=0, message="у студента уже дастаточна денег")
    ])
    institute_name = models.ForeignKey(Institute_name, on_delete=models.CASCADE)
    student_type = models.CharField(max_length=64, choices=TYPE)
    sponsor_deposit = models.ManyToManyField(Sponsor_deposit, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'




