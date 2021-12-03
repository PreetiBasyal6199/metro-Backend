from django.shortcuts import render
from .serializers import navitem_serializer,backgroundSerializer,customer_reviewSerializer,why_metroSerializer,serviceSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import FormParser, JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import background_hero, navbar_items,services,why_metro,customer_review
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.decorators import parser_classes
from rest_framework.generics import ListCreateAPIView
# Create your views here.

@csrf_exempt
def navbar_View(request):
   
    if request.method == 'GET':
        items = navbar_items.objects.all()
        serializer = navitem_serializer(items, many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = navitem_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def update_navbar_View(request,pk):
    try: 
        item = navbar_items.objects.get(pk=pk) 
    except navbar_items.DoesNotExist: 
        return JsonResponse({'message': 'The Item does not exist'}, status=404) 
 
    if request.method =="PUT":
        data = JSONParser().parse(request)
        serializer = navitem_serializer(item,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE': 
        item.delete() 
        return JsonResponse({'message': 'Item was deleted successfully!'}, status=401)      




@csrf_exempt
def background_View(request):
   
    if request.method == 'GET':
        items = background_hero.objects.all()
        serializer = backgroundSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
  



class service_View(ListCreateAPIView):
    queryset = services.objects.all()
    serializer_class = serviceSerializer




class review_View(ListCreateAPIView):
    queryset = customer_review.objects.all()
    serializer_class = customer_reviewSerializer

@csrf_exempt

def why_metro_View(request):
   
    if request.method == 'GET':
        items = why_metro.objects.all()
        serializer = why_metroSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False,status=200)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = why_metroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
