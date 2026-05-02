from django.urls import path
from .views import jobs_list,homePage


urlpatterns = [

    path('result/', jobs_list),
    path('', homePage)
]