from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm
from bs4 import BeautifulSoup
from selenium import webdriver
from django.conf import settings
import re
from matplotlib import pyplot as plt
import numpy as np
from io import BytesIO
import base64


base_dir = settings.BASE_DIR

# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'trends/index.html', context)


def add_keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['input_keywords']
            existing_keyword, created = Keyword.objects.get_or_create(word=keyword)
            existing_keyword.save()
            return redirect("trends:keyword")
    else:
        form = KeywordForm()
    keywords = Keyword.objects.all()
    return render(request, 'trends/keyword.html', {'form': form, 'keywords': keywords})


def keyword_delete(request, pk):
    keywords = Keyword.objects.get(id=pk)
    keywords.delete()
    return redirect("trends:keyword")


def perform_crawling(keyword):
    # 크롬 브라우저 초기화
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)  # 크롬 드라이버 경로 설정

    # 검색어를 이용하여 크롤링
    search_url = f"https://www.google.com/search?q={keyword}"
    driver.get(search_url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # 크롤링 결과 개수 추출
    result_stats = soup.find("div", id="result-stats")

    if result_stats:
        text = result_stats.text
        # 정규 표현식을 사용하여 문자열에서 숫자를 추출
        search_results_count = ''.join(re.findall(r'\d+', text)[:-2])
    else:
        search_results_count = "N/A"

    # 키워드에 대한 크롤링 결과를 Trend 테이블에 저장 또는 업데이트
    try:
        trend = Trend.objects.get(keyword=keyword, search_period='all')
        trend.search_results_count = search_results_count
        trend.save()
    except Trend.DoesNotExist:
        trend = Trend(keyword=keyword, search_results_count=search_results_count, search_period="all")
        trend.save()

    # 크롤링 종료
    driver.quit()

def crawling(request):
    keywords = Keyword.objects.all()

    # 모든 키워드에 대해 크롤링 수행
    for keyword in keywords:
        perform_crawling(keyword.word)

    # 크롤링 결과를 가져와 템플릿에 전달
    trends = Trend.objects.filter(search_period="all")
    return render(request, 'trends/crawling.html', {'trends': trends})


def crawling_histogram(request):
    x = [trend.keyword for trend in Trend.objects.filter(search_period="all")]
    y = [trend.search_results_count for trend in Trend.objects.filter(search_period="all")]
    
    num_values = len(x)
    colors = plt.cm.viridis(np.linspace(0, 1, num_values))

    plt.rcParams['font.family'] = 'Malgun Gothic'
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot()
    ax.set_title('Technology Trend Analysis')
    ax.set_xlabel('Trends')
    ax.set_ylabel('Result')
    ax.tick_params(axis='x', labelrotation=45)
    bars = ax.bar(x, y, color=colors)
    ax.legend(bars, x)
    
    # Save the plot to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_histogram.html', context)


def perform_crawling_advaned(keyword):
    # 크롬 브라우저 초기화
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)  # 크롬 드라이버 경로 설정

    # 검색어를 이용하여 크롤링
    search_url = f"https://www.google.com/search?q={keyword}tbs=qdr:y"
    driver.get(search_url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # 크롤링 결과 개수 추출
    result_stats = soup.find("div", id="result-stats")

    if result_stats:
        text = result_stats.text
        # 정규 표현식을 사용하여 문자열에서 숫자를 추출
        search_results_count = ''.join(re.findall(r'\d+', text)[:-2])
    else:
        search_results_count = "N/A"

    # 키워드에 대한 크롤링 결과를 Trend 테이블에 저장 또는 업데이트
    try:
        trend = Trend.objects.get(keyword=keyword, search_period='year')
        trend.search_results_count = search_results_count
        trend.save()
    except Trend.DoesNotExist:
        trend = Trend(keyword=keyword, search_results_count=search_results_count, search_period="year")
        trend.save()

    # 크롤링 종료
    driver.quit()


def crawling_advaned(request):
    keywords = Keyword.objects.all()

    # 모든 키워드에 대해 크롤링 수행
    for keyword in keywords:
        perform_crawling_advaned(keyword.word)

    x = [trend.keyword for trend in Trend.objects.filter(search_period="year")]
    y = [trend.search_results_count for trend in Trend.objects.filter(search_period="year")]
    
    num_values = len(x)
    colors = plt.cm.viridis(np.linspace(0, 1, num_values))

    plt.rcParams['font.family'] = 'Malgun Gothic'
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot()
    ax.set_title('Technology Trend Analysis')
    ax.set_xlabel('Trends')
    ax.set_ylabel('Result')
    ax.tick_params(axis='x', labelrotation=45)
    bars = ax.bar(x, y, color=colors)
    ax.legend(bars, x)
    
    # Save the plot to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_advaned.html', context)
