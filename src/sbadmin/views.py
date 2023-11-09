from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
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


class IndexView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, "theme/index.html", {})

	def post(self, request, *args, **kwargs):

		return Response({'status': 200})
	
class Map_View2(APIView):
    def get(self, request, *args, **kwargs):
        gdf = gpd.read_file('./geo/daegu_gu_4326.shp')
        
        data = pd.read_csv("./test2.csv")
        data['일3년'] = data['일3년'].astype(object)
        m = folium.Map(location=[35.85788, 128.58918], zoom_start=9)

        cp = folium.Choropleth(geo_data=gdf,
                          name="2010",
                          data=data,
                          key_on='feature.properties.SIG_CD',
                          columns=['SIG_CD', '일3년'],
                          fill_color='YlOrRd',
                          fill_opacity=0.5,
                          line_opacity=0.7,
                          legend_name='학교수',
                          highlight=True).add_to(m)
        
        data_indexed = data.set_index('SIG_KOR_NM')

        for s in cp.geojson.data['features']:
             s['properties']['2010년'] = data_indexed.loc[s['properties']['SIG_KOR_NM'], '일3년']
  
        folium.GeoJsonTooltip(['SIG_KOR_NM', '2010년']).add_to(cp.geojson)
        
        # 툴팁(hover) 추가
        # folium.GeoJsonTooltip(
        #     fields=['SIG_KOR_NM','2010년'],  # 툴팁에 표시할 열 지정
        #     aliases=['행정구 :','학교수 :'],  # 툴팁 열에 대한 별칭 지정
        #     style=('font-weight: bold;')  # 툴팁 스타일 지정
        # ).add_to(cp.geojson)

        folium.LayerControl().add_to(m)
        #folium.GeoJson(gdf).add_to(m)

        m = m._repr_html_()

        return render(request, "theme/index.html", {'map':m})