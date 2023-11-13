from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view
from .serializer import *
import requests

BASE_URL = 'http://finlife.fss.or.kr/'
API_KEY = settings.API_KEY
API_URL = 'finlifeapi/depositProductsSearch.json'

def api_test(request):
    URL = BASE_URL + API_URL
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()

    return JsonResponse({'response':response})

def save_deposit_products(request):
    print('API')
    URL = BASE_URL + API_URL
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
    response = requests.get(URL, params=params).json()
    for item in response['result']['baseList']:
        print(item['fin_prdt_cd'])
        form = DepositProductsSerializer(data=item)
        if form.is_valid():
            print('저장')
            if DepositProducts.objects.filter(fin_prdt_cd=item['fin_prdt_cd']).exists():
                print('이미있음')
                continue
            form.save()
    return JsonResponse({'response':response})




def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return JsonResponse({'response':serializer.data})
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'response': serializer.data})
        else:
            return JsonResponse({ 'message': '이미 있는 데이터이거나, 데이터가 잘못 입력되었습니다.'})    

