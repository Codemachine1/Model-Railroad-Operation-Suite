from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^addCar', views.addCar, name='addCar'),
    url(r'^listCar', views.getCars, name='listCar'),
    url(r'^deleteCar', views.deleteCar, name='deleteCar'),
    url(r'^addLocomotive', views.addLocomotive, name='addLocomotive'),
    url(r'^listLocomotive', views.getLocomotive, name='listLocomotive'),
    url(r'^deleteLocomotive', views.deleteLocomotive, name='deleteLocomotive'),
]