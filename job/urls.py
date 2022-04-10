from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.get_all_jobs, name='jobs'),
    path('jobs/<str:pk>', views.get_job, name='job')
]
