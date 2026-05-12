from django.urls import path
from .views import jobs_list,homePage,save_job,get_saved_jobs


urlpatterns = [

    path('result/', jobs_list),
    path('', homePage),
    path('save-jobs/',save_job),
    path('get/saved-jobs/',get_saved_jobs)
]