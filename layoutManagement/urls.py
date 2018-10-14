from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^addStation', views.addStation, name='addStation'),
    url(r'^showLayout', views.showLayout, name='showLayout'),
    url(r'^deleteStation', views.deleteStation, name='deleteStation'),
    url(r'^addSiding', views.addSiding, name='addLocomotive'),
    url(r'^deleteSiding', views.deleteSiding, name='listLocomotive'),
    url(r'^addYard', views.addYard, name='addYard'),
    url(r'^deleteYard', views.deleteYard, name='deleteYard'),
 ]