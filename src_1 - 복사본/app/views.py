from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User

# from nameapp.models import KospiPredict
from django.views.generic import View
from time import mktime, strptime
import folium
import geopandas as gpd
import pandas as pd
import csv
from rest_framework.renderers import TemplateHTMLRenderer
from django.template.response import TemplateResponse
from django.conf import settings
import os
from django.http import HttpResponse
from django.http import JsonResponse
import json


class IndexView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, "theme/index.html", {})

	def post(self, request, *args, **kwargs):

		return Response({'status': 200})

class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/login.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/register.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class ForgotPasswordView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ChartsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/charts.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class TablesView(APIView):
    def get(self, request):
        
        return render(request, 'theme/tables.html',{})
    
class Tables_result_View(APIView):
    def get(self, request, *args, **kwargs):

        option1 = request.GET['option1']
        option2 = request.GET['option2']

        dt = pd.read_csv("./data/block.csv",encoding="cp949")
        x = _Util(dt)
        res = x._prepData()
        
        results = res.loc[res['LOGI_BUFFER_TIME']>int(option1),:].sort_values(by='RANK').head(int(option2))
        
        results.columns = results.columns.str.replace(' ', '_').str.replace('.', '_')
        # data = pd.concat([data2,data3,data4,data5],axis=1)

        # results = []

        # for i in range(len(data3.columns)):
        #     ff = data[data[data3.columns[i]]==0]["학교명"].count()
        #     results.append(ff)        

        # data = pd.DataFrame(results).T

        # ff = []
        
        # for i in range(len(data3.columns)):
        #     ff.append("필요교원수"+f"{i}")
        

        # data.columns = ff

        json_records = results.to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        
        return render(request, "theme/tables_result.html", context)



class TablesView1(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./table2.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data,
                   'series1_name': '예측년도',
                   'series2_name': 'ARIMA모델',
                   'series3_name': '앙상블모델',
                   'series4_name': 'RNN모델',
                   'series5_name': 'LSTM모델',
                   'series6_name': 'DLinear모델}'}
        
        return render(request, "theme/tables1.html", context)

    
class TablesView2(APIView):
    def get(self, request, *args, **kwargs):
        
        data = pd.read_csv("./table3.csv",encoding="utf-8-sig")

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)

        context = {'df': data,
                   'series1_name': '예측년도',
                   'series2_name': 'ARIMA모델',
                   'series3_name': '앙상블모델',
                   'series4_name': 'RNN모델',
                   'series5_name': 'LSTM모델',
                   'series6_name': 'DLinear모델}'}
        
        return render(request, "theme/tables2.html", context)
    
class TablesView3(APIView):
    def get(self, request, *args, **kwargs):
        results = R1.objects.all()
        return render(request, "theme/tables3.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView4(APIView):
    def get(self, request, *args, **kwargs):
        results = R2.objects.all()
        return render(request, "theme/tables4.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView5(APIView):
    def get(self, request, *args, **kwargs):
        results = R3.objects.all()
        return render(request, "theme/tables5.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView6(APIView):
    def get(self, request, *args, **kwargs):
        results = R4.objects.all()
        return render(request, "theme/tables6.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView7(APIView):
    def get(self, request, *args, **kwargs):
        results = R5.objects.all()
        return render(request, "theme/tables7.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView8(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables8.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
    
class simulation_count_url(APIView):
    def get(self, request):
        
        return render(request, 'theme/simulation_count_url.html',{})

class simulation_count_results_url(APIView):
    
    def get(self, request, *args, **kwargs):
        schoollevel = request.GET['schoollevel']
        prelevel = request.GET['prelevel']
        start_num = request.GET['start_num']
        #end_num = request.GET['end_num']
        limit = request.GET['limit']

        end_num = int(start_num) + 9
        end_num = "년" + str(end_num)
        start_num = "년" + str(start_num)
        

        
        df = pd.read_csv("./예측인원.csv",encoding="utf-8-sig")
        data1 = df[(df["학교유형"]==schoollevel)&(df["예측유형"]==prelevel)]
        data2 = data1.loc[:,"학교명"]
        data3 = data1.loc[:,start_num:end_num]
        data4 = data1.loc[:,"SIG_KOR_NM"]
        data5 = data1.loc[:,"SIG_CD"]

        if (schoollevel=="초등학교"):
            data3 = round(5.939 + 1.404*(data3/int(limit)))
        elif(schoollevel=="중학교"):
            data3 = round(7.701 + 1.720*(data3/int(limit)))
        elif(schoollevel=="고등학교"):
            data3 = round(11.473 + 1.941*(data3/int(limit)))
        
        data = pd.concat([data2,data3,data4,data5],axis=1)

        if (len(data3.columns)==1):
            data.columns = ["학교명","필요교원수","SIG_KOR_NM","SIG_CD"]
        elif (len(data3.columns)==2):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==3):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==4):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==5):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==6):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==7):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==8):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==9):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff
        elif (len(data3.columns)==10):
            ff = []
            ff.append("학교명")
            for i in range(len(data3.columns)):
                ff.append("필요교원수"+f"{i}")
            ff.append("SIG_KOR_NM")
            ff.append("SIG_CD")
            data.columns = ff

        json_records = data.reset_index().to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        

        return render(request, "theme/simulation_count_results_url.html", context)

class simulation_close_url(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/simulation_close_url.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class simulation_close_results_url(APIView):
    
    def get(self, request, *args, **kwargs):
        schoollevel = request.GET['schoollevel']
        prelevel = request.GET['prelevel']
        start_num = request.GET['start_num']
        
        end_num = int(start_num) + 9
        end_num = "년" + str(end_num)
        start_num = "년" + str(start_num)
        
        df = pd.read_csv("./예측인원.csv",encoding="utf-8-sig")
        data1 = df[(df["학교유형"]==schoollevel)&(df["예측유형"]==prelevel)]
        data2 = data1.loc[:,"학교명"]
        data3 = data1.loc[:,start_num:end_num]
        data4 = data1.loc[:,"SIG_KOR_NM"]
        data5 = data1.loc[:,"SIG_CD"]

        data = pd.concat([data2,data3,data4,data5],axis=1)

        results = []

        for i in range(len(data3.columns)):
            ff = data[data[data3.columns[i]]==0]["학교명"].count()
            results.append(ff)        

        data = pd.DataFrame(results).T

        ff = []
        
        for i in range(len(data3.columns)):
            ff.append("필요교원수"+f"{i}")
        

        data.columns = ff

        json_records = data.to_json(orient ='records')
        data = json.loads(json_records)
        context = {'df': data}
        
        return render(request, "theme/simulation_close_results_url.html", context)


# class IndexView(APIView):
#     def visualize_csv(request):
#     # CSV 파일 경로 설정
#         csv_file_path = './src/csv/년도별_총학교수_csv.csv'

#     # CSV 파일 읽기
#         with open(csv_file_path, 'r') as csv_file:
#             reader = csv.reader(csv_file)
#             data = list(reader)

#             labels = [row[0] for row in data[1:]]
#             values = [int(row[1]) for row in data[1:]]

#     # HTML 파일 렌더링
#         return render(request, 'theme/simulation_close.html', {'labels': labels, 'values': values})

#     def post(self, request, *args, **kwargs):

#         return Response({'status': 200})
    
# class indexview2(APIView):
#     def get(self, request, *args, **kwargs):
#         results = all_students_by_year.objects.all()
#         return render(request, "theme/index.html", {'results':results})

#     def post(self, request, *args, **kwargs):

#         return Response({'status': 200})
    
# class KospiPredictAPIView(APIView):

#     authentication_classes = []
#     permission_classes = []

#     def get(self, request):
#         stocks = KospiPredict.objects.all().order_by('date')

#         close_list = []
#         open_list = []
#         for stock in stocks:
#             time_tuple = strptime(str(stock.date), '%Y-%m-%d')  
#             utc_now = mktime(time_tuple) * 1000           
#             close_list.append([utc_now, stock.close])
#             open_list.append([utc_now, stock.open])

#         data = {
#             'close': close_list,
#             'open': open_list
#         }

#         return Response(data)

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'nameapp/chart.html')

class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ButtonsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/buttons.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class CardsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/cards.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class PageNotFoundView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/404.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BlankView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/blank.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ColorsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-color.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BordersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-border.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class AnimationsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-animation.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class OthersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-other.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})



class DashboardView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "users/dashboard.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

# class Map_View(APIView): #시각화 날리는
#     def get(self, request, *args, **kwargs):
#         gdf = gpd.read_file('./geo/tt1/4000x6000.shp')
        
#         data = pd.read_csv("./tt1.csv")
#         data['NUMPOINTS'] = data['NUMPOINTS'].astype(object)
#         m = folium.Map(location=[34.8817, 128.0522], zoom_start=8)

#         cp = folium.Choropleth(geo_data=gdf,
#                           name="2010",
#                           data=data,
#                           key_on='feature.properties.id',
#                           columns=['id', 'NUMPOINTS'],
#                           fill_color='YlOrRd',
#                           fill_opacity=0.5,
#                           line_opacity=0.1,
#                           legend_name='사고수',
#                           highlight=True).add_to(m)
        
#         data_indexed = data.set_index('id')

#         for s in cp.geojson.data['features']:
#              s['properties']['NUMPOINTS'] = data_indexed.loc[s['properties']['id'], 'NUMPOINTS']
  
#         folium.GeoJsonTooltip(['id', 'NUMPOINTS']).add_to(cp.geojson)
        
#         # 툴팁(hover) 추가
#         # folium.GeoJsonTooltip(
#         #     fields=['SIG_KOR_NM','2010년'],  # 툴팁에 표시할 열 지정
#         #     aliases=['행정구 :','학교수 :'],  # 툴팁 열에 대한 별칭 지정
#         #     style=('font-weight: bold;')  # 툴팁 스타일 지정
#         # ).add_to(cp.geojson)

#         folium.LayerControl().add_to(m)
#         #folium.GeoJson(gdf).add_to(m)

#         m = m._repr_html_()
        
#         return render(request, "theme/map.html", {'map':m})

# class Map_View1(APIView): #시각화 날리는
#     def get(self, request, *args, **kwargs):
#         gdf = gpd.read_file('./geo/tt1/4000x6000.shp')
        
#         data = pd.read_csv("./tt1.csv")
#         data['NUMPOINTS'] = data['NUMPOINTS'].astype(object)
#         m = folium.Map(location=[34.8817, 128.0522], zoom_start=8)

#         cp = folium.Choropleth(geo_data=gdf,
#                           name="2010",
#                           data=data,
#                           key_on='feature.properties.id',
#                           columns=['id', 'NUMPOINTS'],
#                           fill_color='YlOrRd',
#                           fill_opacity=0.5,
#                           line_opacity=0.1,
#                           legend_name='사고수',
#                           highlight=True).add_to(m)
        
#         data_indexed = data.set_index('id')

#         for s in cp.geojson.data['features']:
#              s['properties']['NUMPOINTS'] = data_indexed.loc[s['properties']['id'], 'NUMPOINTS']
  
#         folium.GeoJsonTooltip(['id', 'NUMPOINTS']).add_to(cp.geojson)
        
#         # 툴팁(hover) 추가
#         # folium.GeoJsonTooltip(
#         #     fields=['SIG_KOR_NM','2010년'],  # 툴팁에 표시할 열 지정
#         #     aliases=['행정구 :','학교수 :'],  # 툴팁 열에 대한 별칭 지정
#         #     style=('font-weight: bold;')  # 툴팁 스타일 지정
#         # ).add_to(cp.geojson)

#         folium.LayerControl().add_to(m)
#         #folium.GeoJson(gdf).add_to(m)

#         m = m._repr_html_()
        
#         return render(request, "theme/tables1.html", {'map':m})

# class Map_View2(APIView): #인덱스
#     def get(self, request, *args, **kwargs):
#         gdf = gpd.read_file('./geo/daegu_gu_4326.shp')
        
#         data = pd.read_csv("./test2.csv")
#         data['일3년'] = data['일3년'].astype(object)
#         m = folium.Map(location=[35.85788, 128.58918], zoom_start=9)

#         cp = folium.Choropleth(geo_data=gdf,
#                           name="2010",
#                           data=data,
#                           key_on='feature.properties.SIG_CD',
#                           columns=['SIG_CD', '일3년'],
#                           fill_color='YlOrRd',
#                           fill_opacity=0.5,
#                           line_opacity=0.7,
#                           legend_name='학교수',
#                           highlight=True).add_to(m)
        
#         data_indexed = data.set_index('SIG_KOR_NM')

#         for s in cp.geojson.data['features']:
#              s['properties']['2010년'] = data_indexed.loc[s['properties']['SIG_KOR_NM'], '일3년']
  
#         folium.GeoJsonTooltip(['SIG_KOR_NM', '2010년']).add_to(cp.geojson)
        
#         # 툴팁(hover) 추가
#         # folium.GeoJsonTooltip(
#         #     fields=['SIG_KOR_NM','2010년'],  # 툴팁에 표시할 열 지정
#         #     aliases=['행정구 :','학교수 :'],  # 툴팁 열에 대한 별칭 지정
#         #     style=('font-weight: bold;')  # 툴팁 스타일 지정
#         # ).add_to(cp.geojson)

#         folium.LayerControl().add_to(m)
#         #folium.GeoJson(gdf).add_to(m)

#         m = m._repr_html_()

#         return render(request, "theme/index.html", {'map':m})
    

    

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