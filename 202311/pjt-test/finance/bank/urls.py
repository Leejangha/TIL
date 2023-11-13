from django.urls import path, include
from . import views

app_name = 'bank'
urlpatterns = [
    path('', views.api_test),
    # 1. 정기예금 상품 목록 DB에 저장
    path("save-deposit-products/", views.save_deposit_products),
    # 2. 전체 정기예금 상품 목록 출력 & 데이터 삽입
    path("deposit-products/", views.deposit_products),
    # 3. 특정 상품의 옵션 리스트 출력
    # path("deposit-product-options/<str:fin_prdt_cd>", views.deposit_product_options),
]