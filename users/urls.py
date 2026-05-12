from django.urls import path
from .views import signup,protectedProfile

urlpatterns = [
    path('signup/', signup),
    path('profile/', protectedProfile),

]