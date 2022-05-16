import pandas as pd
import numpy as np
from samstag_def import *
import matplotlib.pyplot as plt
import matplotlib 

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus'] = False


# 1. 신용등급별 대출이자 계산 (A:1%, B:3%, C:5%, D:7%)
# 2. 신용등급별 평균 대출이자, 대출금 도넛 그래프그리기

df = pd.read_excel('moka.xlsx')
# print(df.columns)
# print(df[['credit_rating','loan']])
df['대출이자'] = df['credit_rating'].apply(Interest)*df['loan']
money = df.groupby('credit_rating')['대출이자'].mean()
money2 =df.groupby('credit_rating')['loan'].mean()
print(money2)
colors = ['#BF8F73','#D92344','#F2D194','#A61C28']
colors2 = ['#ADD1D9','#3D4025','#6D7345','#D5D973']

plt.subplot(2,2,1)
spaces = [0.2,0.1,0,0]
plt.pie(money,labels=['1등급','2등급','3등급','4등급'],colors = colors,explode=spaces,autopct='%.1f%%',startangle=90,counterclock=False)
plt.title('신용등급별 평균 대출이자')
plt.legend(loc=(1,0.7))

plt.subplot(2,2,2)
plt.pie(money2,labels=['1등급','2등급','3등급','4등급'],colors=colors2,autopct='%.1f',startangle=90,counterclock=False)
plt.title('신용등급별 평균 대출금')
plt.legend(loc=(1,0.7))

plt.show()


