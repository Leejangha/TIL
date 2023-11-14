from django.urls import path, include
from . import views

app_name = 'bank'
urlpatterns = [
    # 1. 정기예금 상품 목록 DB에 저장
    path("deposit/", views.save_deposit_products),
    # 2. 특정 상품의 옵션 리스트 출력
    path("deposit_detail/<str:product_id>", views.deposit_detail),
    # 3. 적금 상품 목록 DB에 저장
    path("saving/", views.save_saving_products),
    # 4. 특정 상품의 옵션 리스트 출력
    path("saving_detail/<str:product_id>", views.saving_detail),
]