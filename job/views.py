from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job

from .serializers import JobSerializer

from django.shortcuts import get_object_or_404


@api_view(['GET'])
def get_all_jobs(request):
    jobs = Job.objects.all()

    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_job(request, pk):
    job = get_object_or_404(Job, id=pk)

    serializer = JobSerializer(job, many=False)

    return Response(serializer.data)
