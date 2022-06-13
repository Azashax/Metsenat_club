from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "numbers", "deposit_Student", "institute_name", "student_type")


@admin.register(Institute_name)
class Institute_nameAdmin(ImportExportModelAdmin):
    list_display = ("id", "name")


@admin.register(Sponsor)
class SponsorAdmin(ImportExportModelAdmin):
    list_display = ("id", "sponsor_name", "numbers", "deposit")


@admin.register(Sponsor_deposit)
class Sponsor_depositAdmin(ImportExportModelAdmin):
    list_display = ("id", "deposit")

