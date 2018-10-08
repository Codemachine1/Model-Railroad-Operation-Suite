from django.shortcuts import render
import json
from models import Cars,Locomotives
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def addLocomotive(request):
	newLocomotive=Locomotives(road_name=request.POST["locomotive_roadname"],
	cartype=request.POST["type"],
	roadNumber=request.POST["number"])
	newLocomotive.save()
	print(newLocomotive.id)
	return HttpResponse(newLocomotive.id)

def deleteLocomotive(request):
	id=int(request.GET.get('id'))
	print(Locomotives.objects.filter(id=id).delete())
	return HttpResponse("okay")

@csrf_exempt
def addCar(request):
	newCar=Cars(road_name=request.POST["roadname"],
	cartype=request.POST["type"],
	roadNumber=request.POST["number"])
	newCar.save()
	
	return HttpResponse(newCar.id)

def deleteCar(request):
	id=int(request.GET.get('id'))
	print(id)
	print(Cars.objects.filter(id=id).delete())
	return HttpResponse("okay")
	
def getLocomotive(request):
	locomotives=Locomotives.objects.all()
	data = serializers.serialize('json', locomotives)
	return HttpResponse(data, content_type="application/json")

def getCars(request):
	cars=Cars.objects.all()
	locomotives=Locomotives.objects.all()
	data = serializers.serialize('json', cars)
	return HttpResponse(data, content_type="application/json")