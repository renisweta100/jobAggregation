from django.urls import path
from .views import signup,protected

urlpatterns = [
    path('signup/', signup),
    path('protected/', protected)
]