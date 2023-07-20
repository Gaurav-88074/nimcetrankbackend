from django.http import HttpResponseBadRequest
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
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
#--------------------------------------------
from .nimcet import printQuestionStats
from .nimcet import computeUserInfo
from .cuet_score_count import computeCuetScore
from django.contrib.auth.models import User
from .models import Person
#-------------------------
# --------serializers-----------
from .serializers import UserSerializer
from .serializers import PersonSerializer

#-----------------------
import random
import json

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# -----------------------------------------------

# -----------------------------------------------
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def signup(request):
    try:
        # print(request.data)
        body = request.data
        # body = json.loads(json.dumps(body))
        # print(body)
        email = body['email']
        password = make_password(body['password'])
        first_name = body['firstname']
        last_name = body['lastname']
        

        UserObject = User.objects.create(
            username=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        UserObject.save()

        PersonObject = Person.objects.create(
            user = UserObject,
            first_name = first_name,
            last_name = last_name,
        )
        PersonObject.save()

        rawData = Person.objects.all()
        serializedData = PersonSerializer(rawData, many=True)
        return Response(serializedData.data)
    except:
        response = {
            'status': 'error', 
            'message': "email id already exists!!"
        }
        indent = 2 
        content = json.dumps(response, indent=indent)
        return HttpResponseBadRequest(content, content_type='application/json')

#------------------------------------------

#-----------------------
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            '0' : 'http://127.0.0.1:8000/admin',
        },
        {
            '1' : 'http://127.0.0.1:8000/login',
        },
        {
            '2' : 'http://127.0.0.1:8000/nimcetscore',
        },
        {
            '3' : 'http://127.0.0.1:8000/token/',
        },
        {
            '4' : 'http://127.0.0.1:8000/token/refresh',
        },
    ]
    return Response(routes)
#-----------------------
@api_view(['POST'])
def getCuetScore(request):
    body = request.data
    # url = "https://cdn.digialm.com//per/g01/pub/1042/touchstone/AssessmentQPHTMLMode1/1042O231/1042O231S1D83/168656844994998/23000453_1042O231S1D83E1.html"

    try:
        url = body['url']
        response = requests.get(url)
        if response.status_code == 200:
            data = response.content
            res = computeCuetScore(data)
            # print(res)
            return Response(res)
    except:
        response = {
            'status': 'error', 
            'message': "Link is invalid"
        }
        indent = 2 
        content = json.dumps(response, indent=indent)
        return HttpResponseBadRequest(content, content_type='application/json')
