from django.shortcuts import render
from django.contrib.auth.models import Group, User, Permission
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def createInitialUser(request):
    if User.objects.filter(groups__name='dispatcher').count()<1:
        newDispatcher=User.objects.create_user(request.POST["Username"],
        request.POST["email"],request.POST["password"])
        newDispatcher.save()
        dispatcherGroup=Group.objects.get(name='dispatcher')
        dispatcherGroup.user_set.add(newDispatcher)
        user=authenticate(username=request.POST["Username"] ,password=request.POST["password"])
        login(request,user)
        return HttpResponseRedirect("/operations")
    else:
        return HttpResponseRedirect("/operations")

def initialUserCreatrionFormPage(request):
    
    new_group, created = Group.objects.get_or_create(name='dispatcher')
    new_group, created = Group.objects.get_or_create(name='operator')
    return render(request,"operations/initalUserCreation.html")
    
def loginPage(request):
    if User.objects.filter(groups__name='dispatcher').count()<1:
        return HttpResponseRedirect("/operations/intialUserCreation")
    else:
        return render(request,"operations/loginPage.html")
    
def loginUser(request):
    user=authenticate(username=request.POST["Username"] ,
                      password=request.POST["password"])
    if user is not None:
        print("user authenticated")
        login(request,user)
        return HttpResponseRedirect("/operations")
    else:
        return HttpResponseRedirect("/operations/loginPage")
        
        
@login_required(login_url='/operations/loginPage')
def mainPage(request):
    if request.user.groups.filter(name="dispatcher").exists():
        return render(request,"operations/dispatcherPage.html")
    else:
        return render(request,"operations/operatorPage.html")