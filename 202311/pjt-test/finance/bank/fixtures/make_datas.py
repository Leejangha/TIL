import random
import requests
import csv
import pandas as pd

# # 현재 API 에 들어있는 금융 상품 코드 리스트 저장
# DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
# SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

# API_KEY = '4e2b65a152ce5ce01b72649b7ea6307f'

# financial_products = []

# params = {
#   'auth': API_KEY,
#   # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
#   'topFinGrpNo': '020000',
#   'pageNo': 1
# }

# # 정기예금 목록 저장
# response = requests.get(DP_URL, params=params).json()
# baseList = response.get('result').get('baseList')   # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])

# # 적금 목록 저장
# response = requests.get(SP_URL, params=params).json()
# baseList = response.get('result').get('baseList')   # 상품 목록

# for product in baseList:
#     financial_products.append(product['fin_prdt_cd'])

# dict_keys = ['salary', 'gender', 'financial_products']

# random_choices = financial_products

df = pd.read_csv('C:/Users/SSAFY/Desktop/finalPJT - 복사본/pjt-test/finance/bank/fixtures/bank2.csv', encoding='utf-8')

df["gender"]

# # 원본 CSV 파일 이름
# input_filename = "bank2.csv"

# # 결과를 저장할 새로운 CSV 파일 이름
# output_filename = "user_data2.csv"

# with open(input_filename, mode='r', encoding='utf-8') as infile:
#     reader = csv.reader(infile)
#     rows = list(reader)

# # 새 열 추가 (첫 번째 행이 헤더라고 가정)
# rows[0].append("salary")
# # rows[0].append("gender")
# # rows[0].append("financial_products")


# # 각 행에 대해 랜덤한 값을 선택하여 새 열에 추가
# for row in rows[1:]:
#     row.append(random.choice(random_choices))
# # for row in rows[1:]:
# #     row.append(random.choice(random_choices))
# # for row in rows3[1:]:
# #     row.append(random.choice(random_choices))

# # 수정된 내용을 새 파일에 저장
# with open(output_filename, mode='w', encoding='utf-8', newline='') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerows(rows)
