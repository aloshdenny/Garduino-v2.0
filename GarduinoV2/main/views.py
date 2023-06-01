from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import PlantData
from main.serializers import ArduinoSerializer

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

# API views
@csrf_exempt
def get_alldata(request):
    """
    Modify/List all plant data
    """
    if request.method == "GET":
        plants = PlantData.objects.all()
        serializer = ArduinoSerializer(plants, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArduinoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        
        return JsonResponse(serializer.errors, status=400)

# Single value handling
@csrf_exempt
def modify_singleplant(request, pk):
    """
    Modify/List single plant data
    """

    try:
        plant = PlantData.objects.get(pk=pk)
    except PlantData.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ArduinoSerializer(plant)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArduinoSerializer(plant, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        plant.delete()
        return HttpResponse(status=204)