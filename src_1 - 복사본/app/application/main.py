# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:02:25 2024

@author: USER
"""

import src.utils as utils
import pandas as pd

dt = pd.read_csv('block.csv', encoding = 'cp949')

x = utils._Util(dt)
res = x._prepData()
results = res.loc[res['LOGI_BUFFER_TIME']>5,:]
results = res.loc[res['LOGI_BUFFER_TIME']>int(option1),:].sort_values(by='RANK').head(int(option2))

# 블록크기 -> A.proj_NC -> 뒤에 두개         
results.loc[:,'A.PROJ_NO'].str[4:-1].value_counts()
results.loc[:,'A.BLK_NO'].str[3:-1].value_counts()


results.loc[:,'LOGI_BUFFER_TIME'].value_counts()
results.loc[:,'ISOP_BUFFER_TIME'].value_counts()



results.loc[:,"LOGI_CHK_DESC"].value_counts()
results.columns

logi_buffer_time
ISOP_BUFFER_TIME


results.loc[:,"후공정 대기 기간"].value_counts()

letter_counts = df['first_two_letters'].value_counts()

# 1. 로그인
# 2. 파일업로드
# 3. 옵션선택
# 4. 결과 도출 -> progress바 추가

# 5. 알고리즘 결합 -> 추가해서 나중에

# 옵션
# LOGI_BUFFER_TIME 이상으로 
# LOGI_BUFFER_TIME 랭킹으로 -> 갯수 ? 

# logi_buffer_time -> 화면에 나오게
# 1일 이상

# 사외반출입 블록 관리 시스템 -> 타이틀 
# 사외반출입 최적 블록 선정 -> 

# 사외반출입 최적 블록 선정 시뮬레이션
# 사외반출입 선정 블록 분석 결과
# 사외반출입 물류 스케줄 최적화