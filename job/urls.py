from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.get_all_jobs, name='jobs'),
    path('jobs/<str:pk>', views.get_job, name='job'),
    path('jobs/new/', views.post_job, name='new_job'),
    path('jobs/<str:pk>/delete', views.delete_job, name='delete_job'),
    path('jobs/<str:pk>/update', views.update_job, name='update_job'),
    path('stats/<str:topic>/', views.get_topic_stats, name='get_topic_stats'),
]
