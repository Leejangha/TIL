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
import seaborn as sns 

# 예금 리스트 load
current_directory = os.path.dirname(os.path.abspath(__file__))
product_json = open(current_directory+'/product_list.json', encoding='utf-8')
product_list = json.load(product_json)

# 유저 데이터 load
# df_user = pd.read_csv(current_directory+'/data.csv')
# df_user['gender'] = pd.to_numeric(df_user['gender'], errors='coerce')

json_file_path = os.path.join(current_directory, 'user_data.json')
with open(json_file_path, 'r', encoding='utf-8') as file:
    user_data = json.load(file)
df_user = pd.DataFrame(user_data)

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

# 실루엣 계수로 k 값 찾기
# fig, ax = plt.subplots(3, 2, figsize=(15,8))
# for i in [3, 4, 5, 6, 7]:
#     km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=0)
#     q, mod = divmod(i, 2)
#     visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
#     visualizer.fit(data_scaled)
# visualizer.show()

k = 4

# 모델 생성
kmeans  = KMeans(n_clusters=k, init='k-means++', max_iter=300, random_state=0, n_init=10)

# 모델 훈련
kmeans.fit(data_scaled)

# 유저 군집 라벨 추가
df_user['cluster'] = kmeans.labels_

user_cluster = df_user['cluster'].iloc[-1]

# # 시각화
# centers_s = kmeans.cluster_centers_

# plt.figure(figsize=(20, 6))

# X = df_user

# plt.subplot(131)
# sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,1], data=df_user, hue=kmeans.labels_, palette='coolwarm')
# plt.scatter(centers_s[:,0], centers_s[:,1], c='black', alpha=0.8, s=150)

# plt.subplot(132)
# sns.scatterplot(x=X.iloc[:,1], y=X.iloc[:,2], data=df_user, hue=kmeans.labels_, palette='coolwarm')
# plt.scatter(centers_s[:,1], centers_s[:,2], c='black', alpha=0.8, s=150)

# plt.subplot(133)
# sns.scatterplot(x=X.iloc[:,2], y=X.iloc[:,3], data=df_user, hue=kmeans.labels_, palette='coolwarm')
# plt.scatter(centers_s[:,2], centers_s[:,3], c='black', alpha=0.8, s=150)

# plt.show()

# 동일한 클러스터에 있는 사용자의 금융 상품 추출
financial_products = df_user.loc[df_user['cluster'] == user_cluster, 'financial_products']


# 상품별 개수 계산
product_count = dict(Counter(item for sublist in [s.split(',') for s in financial_products] for item in sublist))
print(len(product_count.keys()))

# 개수별로 제품 정렬
sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)

# 추천상품 표시
recommend_list = []
for product, count in sorted_products[:6 ]:
    if product != '':
        recommend_list.append(product)
print(recommend_list)
