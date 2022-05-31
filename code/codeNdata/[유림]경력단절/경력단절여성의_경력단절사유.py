#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='NanumGothic')

df = pd.read_csv('경력단절여성의 경력단절 사유.csv',encoding='cp949')


# In[15]:


#전체 데이터 중 사유별 비율 데이터만 가져옴. (비율, 단위:%)
# 행, 열 삭제 https://benn.tistory.com/27   /   https://www.delftstack.com/ko/howto/python-pandas/how-to-delete-pandas-dataframe-column/


df=df.loc[[3,5,7,9,11],'구분별':'2021 년']


# In[16]:


#필요없는 열 삭제
df = df.drop(['항목','단위'], axis=1)


# In[17]:


df=df.T


# In[18]:


df.columns=['결혼준비','임신,출산','자녀교육(초등학생)','가족돌봄','육아']
df


# In[19]:


df = df.drop('구분별',axis=0)


# In[20]:


df = df.reset_index()


# In[21]:


df=df.rename(columns={'index':'연도'})
df


# In[22]:


import platform
if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        #!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
        #!mv malgun.ttf /usr/share/fonts/truetype/
        #import matplotlib.font_manager as fm 
        #fm._rebuild() 
        plt.rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결


# In[24]:


plt.rcParams['figure.figsize'] = [12, 8]
plt.plot(df['연도'], df['결혼준비'], marker='s', color='r', label='결혼준비')
plt.plot(df['연도'], df['임신,출산'], marker='o', color='g', label='임신,출산')
plt.plot(df['연도'], df['자녀교육(초등학생)'], marker='*', color='b', label='자녀교육(초등학생)')
plt.plot(df['연도'], df['가족돌봄'], marker='+', color='y', label='가족돌봄')
plt.plot(df['연도'], df['육아'], marker='+', color='violet', label='육아')

plt.title('경력단절여성의 경력단절 사유(2011-2021)', fontsize=20) 
plt.ylabel('비율', fontsize=14)
plt.xlabel('연도', fontsize=14)
plt.legend(fontsize=12, loc='best')

plt.savefig('경력단절여성의 경력단절 사유.png')


# In[ ]:





# In[ ]:




