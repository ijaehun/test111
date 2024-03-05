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
	
class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/login.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})