from django.shortcuts import render
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from io import BytesIO
import base64
from django.conf import settings


base_dir = settings.BASE_DIR


plt.switch_backend('Agg')
pd.plotting.register_matplotlib_converters()

# Create your views here.
def index(request):
    context = {
    }

    return render(request, 'weathers/index.html', context)


csv_path = f'{base_dir}/weathers/data/austin_weather.csv'


def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df' : df,
    }
    return render(request, 'weathers/problem1.html', context)


def problem2(request):
    df = pd.read_csv(csv_path)
    df["Date"] = pd.to_datetime(df["Date"])

    plt.figure(figsize=(12,7))
    plt.title('Temperature Variation')
    plt.plot(df['Date'], df['TempHighF'], label='HighTemperature')
    plt.plot(df['Date'], df['TempAvgF'], label='AvgTemperature')
    plt.plot(df['Date'], df['TempLowF'], label='LowTemperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenehit)')
    plt.legend(loc = 8)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf8').replace('\n', '')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    df = pd.read_csv(csv_path)
    df["Date"] = pd.to_datetime(df["Date"])
    month_df = df.groupby(df['Date'].dt.to_period('M'))

    monthly_mean = pd.DataFrame(index=pd.date_range(start=df["Date"].iloc[0], end=df["Date"].iloc[-1], freq='M'))
    monthly_mean['TempHighF'] = month_df['TempHighF'].mean().values
    monthly_mean['TempAvgF'] = month_df['TempAvgF'].mean().values
    monthly_mean['TempLowF'] = month_df['TempLowF'].mean().values
    monthly_mean

    plt.figure(figsize=(12,7))
    plt.title('Temperaure Variation')
    plt.plot(monthly_mean['TempHighF'], label='HighTemperature')
    plt.plot(monthly_mean['TempAvgF'], label='AvgTemperature')
    plt.plot(monthly_mean['TempLowF'], label='LowTemperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenehit)')
    plt.legend(loc = 4)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf8').replace('\n', '')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    df = pd.read_csv(csv_path)
    df = df['Events']
    df = df.replace(np.nan,'No Events')
    df_split = df.str.split(',', expand=True).stack().str.strip()
    df_split = df_split.reset_index(level=1, drop=True).rename('Events')
    event_counts = df_split.value_counts(dropna = False).reset_index()
    event_counts.columns = ['Events', 'Count']

    plt.figure(figsize=(10, 6))
    plt.bar(event_counts['Events'], event_counts['Count'])
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Event Counts')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf8').replace('\n', '')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'weathers/problem4.html', context)