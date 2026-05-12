from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .serializer import JobSerializer
from .models import Jobs,SavedJob
from rest_framework.response import Response
from .services import filter_job
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def homePage(request):
    return render(request, 'home.html')





@api_view(['GET'])
def jobs_list(request):
    search = request.GET.get('search')
    jobs = filter_job.filter_job_funct(search)
    return Response(jobs)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_saved_jobs(request):
    saved_jobs = SavedJob.objects.filter(user=request.user)
    data=[]
    for job in saved_jobs:
         data.append({
             "title": job.title,
             "company": job.company
         })
    return Response(data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_job(request):
    title = request.data.get("title")
    company = request.data.get("company")

    SavedJob.objects.create(
    user=request.user,
    title=title,
    company=company

    )
    return Response({"message": "Job Saved successfully"})



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