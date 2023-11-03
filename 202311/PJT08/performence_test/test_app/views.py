from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import random
from django.conf import settings
import numpy as np
import pandas as pd

base_dir = settings.BASE_DIR


csv_path = f'{base_dir}/test_app/data/test_data.csv'

def data(request):
    df = pd.read_csv(csv_path, encoding='cp949')
    data = df.to_dict('records')
    print(df.columns)

    context = {
        'data': data,
    }

    return JsonResponse(context)


csv_path_has_null = f'{base_dir}/test_app/data/test_data_has_null.csv'

def imputation(request):
    df = pd.read_csv(csv_path_has_null, encoding='cp949').fillna('NULL')
    data = df.to_dict('records')

    context = {
        'data': data,
    }

    return JsonResponse(context)


df = pd.read_csv(csv_path_has_null, encoding='cp949')

def mean(request):
    avg = df['나이'].mean()
    df['편차'] = abs(df['나이'] - avg)
    # df.dropna(subset=['나이'], inplace=True)
    data = df.sort_values(by='편차').head(10).to_dict('records')

    context = {
        'data': data,
    }

    return JsonResponse(context)


array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)
