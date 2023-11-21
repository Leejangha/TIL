import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os
import csv
from yellowbrick.cluster import KElbowVisualizer
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from collections import Counter
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, confusion_matrix

# 예금 리스트 load
current_directory = os.path.dirname(os.path.abspath(__file__))
product_json = open(current_directory+'/product_list.json', encoding='utf-8')
product_list = json.load(product_json)

# 유저 데이터 load
df_user = pd.read_csv(current_directory+'/data.csv')
df_user['gender'] = pd.to_numeric(df_user['gender'], errors='coerce')

# 결측치 확인
# print(df_user.isnull().sum())

# features 선택
data = df_user[['age','gender', 'money', 'salary']]

# 정규화 진행
scaler = MinMaxScaler()
scaler.fit(data)

# 정규화 계산
data_scaled = scaler.transform(data)

# # elbow 기법으로 k 값 찾기
# km = KMeans(n_init=10, random_state=0)
# visualizer = KElbowVisualizer(km, k=(2,10))
# visualizer.fit(data_scaled)
# visualizer.show()

# # 실루엣 계수로 k 값 찾기
# fig, ax = plt.subplots(3, 2, figsize=(15,8))
# for i in [3, 4, 5, 6, 7]:
#     km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=0)
#     q, mod = divmod(i, 2)
#     visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
#     visualizer.fit(data_scaled)
# visualizer.show()

k = 4

# 모델 생성
model = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state=0, n_init=10)

# 모델 훈련
model.fit(data_scaled)

km = model.labels_

df_user['cluster'] = km


# # K-means 군집화
# kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, random_state=0, n_init=10)
# kmeans.fit(X_scaled)
# labels = kmeans.labels_



# df_user['cluster'] = kmeans.fit_predict(X_scaled)

# # k = 4

# # plt.figure(figsize = (8, 8))

# # for i in range(k):
# #     plt.scatter(df_user.loc[df_user['cluster'] == i, 'gender'], df_user.loc[df_user['cluster'] == i, 'money'], 
# #                 label = 'cluster ' + str(i))

# # plt.legend()
# # plt.title('K = %d results'%k , size = 15)
# # plt.xlabel('Gender', size = 12)
# # plt.ylabel('Money', size = 12)
# # plt.show()


# # 유저 군집 라벨 선택
# labels = kmeans.labels_
# df_user['cluster_label'] = labels
# user_cluster = df_user['cluster_label'].iloc[-1]


# # 동일한 클러스터에 있는 사용자의 금융 상품 추출
# financial_products = df_user.loc[df_user['cluster_label'] == user_cluster, 'product']


# # 상품별 개수 계산
# product_count = dict(Counter(','.join(financial_products).split(';')))

# # 개수별로 제품 정렬
# sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

# # 추천상품 표시
# recommend_list = []
# for product, count in sorted_products[:6 ]:
#     if product != '':
#         recommend_list.append(product)
# print(recommend_list)
