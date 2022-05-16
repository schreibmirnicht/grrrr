import pandas as pd
import numpy as np 
from samstag_def import *
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='AppleGothic'
matplotlib.rcParams['font.size']=10
matplotlib.rcParams['axes.unicode_minus']=False



# 1. 판다스 데이터 프레임으로 변환
# 2. 생활비 컬럼생성 - 단위행렬 곱을 이용해서 단위를 “만원”으로 통일
# 3. 연령대(10대,20대~90대)&성별 당 생활비 평균 가로막대그래프 그리기
#대출금 백만원// 전자기기 만원 // 간식비 

df = pd.read_excel('moka.xlsx')

# print(df['appliances '])
# print(df['snack'])
# print(df['clothes'])

arr1 =np.array([df['appliances '],df['snack'],df['clothes']])
arr2 = np.array([1,0.0001,10])

print(df.columns)

df['living_expenses']=np.dot(arr2,arr1)
 
# print(df['living_expenses'])

# print(df.columns)


df['Age_line'] = df['age'].apply(all_Age)
print(df['Age_line'])
fm = df.groupby(['gender','Age_line'])['living_expenses'].mean()[:9]
mm = df.groupby(['gender','Age_line'])['living_expenses'].mean()[9:]
y = ['10대','20대','30대','40대','50대','60대','70대','80대','90대']
y1 = np.arange(9)
print(fm)

plt.xlabel('생활비평균(만원)')
plt.ylabel('연령대(세)')
plt.barh(y1,-mm,label='남자')
plt.barh(y1,fm,label='여자')
plt.yticks(y1,y)
plt.legend()


for i in range(len(mm)):
    plt.text(-mm[i]+100,y1[i]-0.2,mm[i],ha='center') 
    
    
plt.show()






