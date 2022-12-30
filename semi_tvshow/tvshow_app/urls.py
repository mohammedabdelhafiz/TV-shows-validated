from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new', views.index),	   
    path('addshow', views.addshow),
    path('showtwo/<int:id>',views.showtwo),

]