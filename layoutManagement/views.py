from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from models import station, siding, yard
# Create your views here.
@csrf_exempt
def addSiding(request):
    stationToAddSidingTo=station.objects.get(id=request.POST["stationID"])
    stationToAddSidingTo.siding_set.create(name=request.POST["name"],milePost=request.POST["milepost"])
    stationToAddSidingTo.save()
    return HttpResponse(stationToAddSidingTo.id)

@csrf_exempt
def addStation (request):
    newStation=station(name=request.POST["name"],milePost=request.POST["milepost"])
    newStation.save()
    return HttpResponse("okay")

@csrf_exempt
def addYard(request):
    stationToAddYardTo=station.objects.get(id=request.POST["stationID"])
    stationToAddYardTo.siding_set.create(name=request.POST["name"],milePost=request.POST["milepost"])
    stationToAddYardTo.save()
    return HttpResponse(stationToAddYardTo.id)
    
def deleteSiding(request):
    sidingId=request.GET["sidingId"]
    siding.objects.filter(id=sidingId).delete()
    return HttpResponse("okay")
    
def deleteStation(request):
    stationId=request.GET["stationId"]
    station.objects.filter(id=stationId).delete()
    return HttpResponse("okay")
    
def deleteYard(request):
    yardId=request.GET["yardId"]
    yard.objects.filter(id=yardId).delete()
    return HttpResponse("okay")
    
def showLayout(request):
    layout=station.objects.order_by("milePost").all()
    data = serializers.serialize('json',layout )
    return HttpResponse(data)