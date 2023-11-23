import random
import requests
import pandas as pd
import numpy as np

# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '4e2b65a152ce5ce01b72649b7ea6307f'

financial_products = []

params = {
  'auth': API_KEY,
  # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
  'topFinGrpNo': '020000',
  'pageNo': 1
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')   # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])



file_path = 'fin_data.csv'
df = pd.read_csv(file_path)


df = df[['age', 'money', 'gender', 'salary']]



df['product'] = df.apply(lambda row: random.sample(financial_products, random.randint(0, 5)), axis=1)


# # for column in columns_to_modify:
# #     df[column] = [random.randrange(0, 1500000000, 1000000) for _ in range(len(df))]
# print("Current data type of 'money' column:", df['money'].dtype)

# # Convert to absolute values
# df['money'] = np.abs(df['money'])

# # Print the number of negative values (just to double-check)
# print("Number of negative values:", len(df.loc[df['money'] < 0]))
output_file_path = 'fin_data2.csv'  # Replace with the desired output file path
df.to_csv(output_file_path, index=False, float_format='%.0f')

# print(f"Updated DataFrame saved to {output_file_path}")
# # dict_keys = ['gender', 'age', 'money', 'salary', 'financial_products']

# json 파일 만들기
# import json
# from collections import OrderedDict

# file = OrderedDict()

# N = 10000
# i = 0

    
# # 저장 위치는 프로젝트 구조에 맞게 수정합니다.
# save_dir = 'bank/fixtures/user_data.json'
# with open(save_dir, 'w', encoding="utf-8") as f:
#     f.write('[')
#     for i in range(N):
#         file["model"] = "accounts.User"
#         file["pk"] = i+1
#         file["username"]= username_list[i]
#         file["financial_products"]= ','.join([random.choice(financial_products) for _ in range(random.randint(0, 5))]) # 금융 상품 리스트
#         file["gender"]= random.choice(['1','2'])
#         file["age"]= random.randrange(0, 100, 1)  # 나이
#         file["money"]= random.randrange(0, 1500000000, 1000000)    # 현재 가진 금액
#         file["salary"]= random.randrange(0, 1500000000, 1000000) # 연봉

#         json.dump(file, f, ensure_ascii=False, indent="\t")
#         if i != N-1:
#             f.write(',')
#     f.write(']')
#     f.close()

# print(f'데이터 생성 완료 / 저장 위치: {save_dir}')