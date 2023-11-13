from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions

# Form -> forms.Form / forms.ModelForm
# serializers -> Serializer / ModelSerializer

# Model이 붙으면 -> 정의한 필드에 대해서 입출력
# 안붙으면 -> 사용자가 원하는 필드를 추가로 입력 받거나, 출력함
class DepositProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositProducts
    fields = '__all__'
    
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_firels = ('fin_prdt_cd',)

class SavingProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = SavingProducts
    fields = '__all__'
    
class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_firels = ('fin_prdt_cd',)
