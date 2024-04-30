from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

SECONDS_LEFT = 23334

@api_view(['GET'])
def time_left(request):
    if request.method == 'GET':
        return Response({'secondsLeft': SECONDS_LEFT})
