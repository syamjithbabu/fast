from django.urls import path
from . import views

app_name='you'

urlpatterns = [
    path('',views.Time,name='united'),
    path('hi/',views.Hai,name='no'),
    path('do/',views.Go,name='long'),
]
