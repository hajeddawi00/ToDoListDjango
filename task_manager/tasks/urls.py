from django.urls import path
from . import views
app_name = "tasks"
urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('complete/<task_id>/', views.complete_task, name='complete_task'),
    path('delete/<task_id>/', views.delete_task, name='delete_task')
]