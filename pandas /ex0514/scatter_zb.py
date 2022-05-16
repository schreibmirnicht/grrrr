import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from samstag_def import *

matplotlib.rcParams['font.family'] ='AppleGothic'
matplotlib.rcParams['font.size']=10
matplotlib.rcParams['axes.unicode_minus']=False

df = pd.read_excel('moka.xlsx')

df['Age_line'] = df['age'].apply(all_Age)

# print(df.groupby(['Age_line'])['snack'].count())
# print(df.groupby(['Age_line'])['appliances '].count())

y = df['appliances ']
x = df['snack']
sticks = np.arange(10,100,10)
plt.scatter(x,y,s=100,c=df['Age_line'],cmap='RdYlGn')
plt.title('간식 & 전자기기')
plt.colorbar(ticks=sticks,label='연령대')
plt.xlabel('간식비(원)',fontsize= 10)
plt.ylabel('전자기기(만원',fontsize =10)
plt.show()


# # 4. 전자-간식 산점도 그래프 그리기
# plt.scatter(df['snack'],df['appliances'],s=100,c=df['ageBlock'],cmap='viridis')
# plt.colorbar(ticks=[10,20,30,40,50,60,70,80,90],label='연령대')
# plt.title('간식-전자기기 관계')
# plt.xlabel('간식비(단위:원)',fontsize=10)
# plt.ylabel('전자기기(단위:만원)',fontsize=10)
# plt.show()



#y축 전자기기 단위
#x축 간식비 단위
#컬러바 연령대