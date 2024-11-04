
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks/', include('tasks.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('login/staff/', views.login_view, name='login_staff'),
]
