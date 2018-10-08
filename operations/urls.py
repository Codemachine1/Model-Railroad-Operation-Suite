from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='index'),
    url(r'^loginPage', views.loginPage, name='login'),
    url(r'^loginUser', views.loginUser, name='loginUser'),
    url(r'^intialUserCreation', views.initialUserCreatrionFormPage, name='intialUserCreationForm'),
    url(r'^createInitialUser', views.createInitialUser, name='createInitialUser'),

]