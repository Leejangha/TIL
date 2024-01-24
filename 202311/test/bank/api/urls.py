from django.urls import path, include
from .import views

app_name = 'api'
urlpatterns = [
    path('', views.save_deposit_prodeucts),
]

