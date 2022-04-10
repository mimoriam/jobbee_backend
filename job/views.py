from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job

from .serializers import JobSerializer


@api_view(['GET'])
def get_all_jobs(request):
    jobs = Job.objects.all()

    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data)
