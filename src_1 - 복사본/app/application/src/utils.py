# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:54:22 2024

@author: USER
"""

import pandas as pd

class _Util(object):
    
    def __init__(self, dt):
        self.dt = dt
        
    def _prepData(self):
        
        self.dt['CHECK_CUR_JOB'] = self.dt['A.IA_NOW_P_STG'].apply(lambda x:self._checkCurrentJob(x))
        self.dt['CHECK_NEXT_JOB'] = self.dt['AF_CODE_DESC'].apply(lambda x:self._checNextJob(x))
        self.dt['LOGI_BUFFER_TIME'] = self.dt.apply(lambda x:self._calculateTime(x['IA_AF_STDT'],x['LOGI_CHK_DT'], x['CHECK_NEXT_JOB'] ), axis=1)
        self.dt['ISOP_BUFFER_TIME'] = self.dt.apply(lambda x:self._calculateTime(x['IA_AF_STDT'],x['A.IA_NOW_FNDT'], x['CHECK_NEXT_JOB']), axis=1)
        self.dt['CHECK_SIZE'] = self.dt['A.BLK_NO'].apply(lambda x:self._checkSize(x))
        self.dt['CHECK_DAY_NIGHT'] = self.dt['WKA_CD'].apply(lambda x:self._checkDayNight(x))
        self.dt = self.dt.sort_values(by=['LOGI_BUFFER_TIME', 'ISOP_BUFFER_TIME', 'CHECK_DAY_NIGHT', 'CHECK_SIZE'])[::-1].reset_index(drop=True)
        self.dt['RANK'] = range(1,len(self.dt)+1)
        return self.dt
    
    def _checkDayNight(self, x):
        if x == '51BAY' or x == '52BAY':
            v = 1
        else:
            v = 0
        return v
        
    def _checkSize(self, x):
        
        if x[-2:] == 'UC' or x[-2:] == 'VC':
            v = 0
        else:
            v = 1
        return v

    def _calculateTime(self, x,y,z):

        if str(x)!='nan' and str(y)!='nan' :
            v = pd.to_datetime(str(int(x))) - pd.to_datetime(str(int(y)))
        else:
            v = pd.to_datetime(pd.Timestamp(year=1900, month=1, day=1).date()) - pd.to_datetime(pd.Timestamp(year=2000, month=1, day=1).date())
        if z == '3':
            res = v.days-2
        else:
            res = v.days
        return res

    def _checkCurrentJob(self, x):
        if '장' in list(str(x)):
            if '도' in list(str(x)):
                v = 3
            elif '의' in list(str(x)):
                v = 2
        elif '조' and '립' in list(str(x)):
            v = 1
        else:
            v = 0
        return v

    def _checNextJob(self,x):
        
        if '장' in list(str(x)):
            if '도' in list(str(x)):
                v = 3
            elif '의' in list(str(x)):
                v = 2
        elif '조' and '립' in list(str(x)):
            v = 1
        else:
            v = 0
        return v
        