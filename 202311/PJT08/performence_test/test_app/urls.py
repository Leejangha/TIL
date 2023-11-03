from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data, name='data'),
    path('imputation/', views.imputation, name='imputation'),
    path('mean/', views.mean),
    path('normal_sort/', views.normal_sort),
    path('priority_queue/', views.priority_queue),
    path('bubble_sort/', views.bubble_sort),
]

