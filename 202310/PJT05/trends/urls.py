from django.urls import path
from . import views

app_name = 'trends'
urlpatterns = [
    path('', views.index),
    path('keyword/', views.add_keyword, name='keyword'),
    path('keyword/<int:pk>/', views.keyword_delete, name='keyword_delete'),
    path('crawling/', views.crawling, name='crawling'),
    path('crawling/histogram/', views.crawling_histogram, name='crawling_histogram'),
    path('crawling/advaned/', views.crawling_advaned, name='crawling_advaned'),
]
