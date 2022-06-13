from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('sponsor/', views.SponsorListCreateAPIView.as_view()),
    path('sponsor/<str:pk>', views.SponsorRetrieveUpdateDestroyAPIView.as_view()),

    path('sponsor_deposit/', views.Sponsor_depositListCreateAPIView.as_view()),
    path('sponsor_deposit/<str:pk>', views.Sponsor_depositRetrieveUpdateDestroyAPIView.as_view()),

    path('student/', views.StudentListCreateAPIView.as_view()),
    path('student/<str:pk>', views.StudentDetailView.as_view()),

    path('dashboard/', views.DashboardAPIView.as_view()),


]
