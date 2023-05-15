"""
URL configuration for login_project project.

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
from django.contrib import admin
from django.urls import path
from login_app.views import *
from register_app.views import *
from connection_app.views import *
from connection_details_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('conn_details/',Connectiton_Detail_View.as_view()),
    path('conn_details/<int:pk>/', Connectiton_Detail_View.as_view()),
    path('conn_get/<int:pk>/',List_Connections_View.as_view()),
    path('conn_get',List_Connections_View.as_view()),
    path('login/',Login_View.as_view()),
    path('register/',RegisterView.as_view()),
    path('conn_post',Create_Connections_View.as_view()),
    path('conn_delete/<int:pk>/',Delete_Connections_View.as_view()),
    path('conn_put/<int:pk>/',Update_Connections_View.as_view())
]

