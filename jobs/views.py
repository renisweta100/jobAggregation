from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .serializer import JobSerializer
from .models import Jobs
from rest_framework.response import Response
from .services import filter_job

# Create your views here.


def homePage(request):
    return render(request, 'home.html')





@api_view(['GET'])
def jobs_list(request):
    search = request.GET.get('search')
    jobs = filter_job.filter_job_funct(search)
    return Response(jobs)



    """
    if request.method == "GET":
        job_extract=Jobs.objects.all()
        serializer = JobSerializer(job_extract, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = JobSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.error, status=201)

"""