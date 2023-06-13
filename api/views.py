from django.shortcuts import render
import imp
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import requests
from bs4 import BeautifulSoup
import requests
from .nimcet import printQuestionStats
# Create your views here.
# Create your views here.
#-------------------------

#-----------------------
import random
import json
#-----------------------
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            '1' : 'http://127.0.0.1:8000/allvocab',
        },
        {
            '2' : 'https://vocabapi2023-production.up.railway.app/allvocab',
        },
        {
            '2' : 'https://vocabapi2023-production.up.railway.app/addvocab',
        }
    ]
    return Response(routes)
#-----------------------
@api_view(['GET'])
def getNimcetScore(request):
    url = "https://cdn.digialm.com//per/g01/pub/1042/touchstone/AssessmentQPHTMLMode1/1042O231/1042O231S1D83/168656844994998/23000453_1042O231S1D83E1.html"
    response = requests.get(url)
    if response.status_code == 200:
    
        data = response.content
        
        soup = BeautifulSoup(data, 'html.parser')
        # soup.find('div', class_="question-pnl")
        # print(soup.prettify())
        questions = soup.find_all(class_='question-pnl')
        return Response(printQuestionStats(questions[:120]))
    else:
        return Response([{"message":"some sort of error"}])
