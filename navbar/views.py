from django.shortcuts import render
from .serializers import navitem_serializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import navbar_items
# Create your views here.

@csrf_exempt
def navbar_View(request):
   
    if request.method == 'GET':
        transformer = navbar_items.objects.all()
        serializer = navitem_serializer(transformer, many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = navitem_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


