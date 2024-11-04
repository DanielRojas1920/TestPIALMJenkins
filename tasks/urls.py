from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/add_task/', views.add_task, name='add_task'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
