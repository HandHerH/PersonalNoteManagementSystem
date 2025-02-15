"""
URL configuration for PersonalNoteManage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from UserManage import views

app_name = 'AppUserManage'

urlpatterns = [
    path(r'main/', views.MainPageView.as_view(), name='main'),
    path(r'register/', views.RegisterView.as_view(), name='register'),
    path('a/send_verify_code/', views.EmailView.as_view(), name='send_verify_code'),
]
