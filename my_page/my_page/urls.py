
from django.urls import path
from . import views


urlpatterns = [
    path('horoscope/leo/', views.leo),
    path('horoscope/scorpio/', views.scorpio),
]
