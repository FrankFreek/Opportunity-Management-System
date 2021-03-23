"""opportunitiesmgt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from opportunitiesmgt_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),
    path('signup/', views.signupPage, name='signup'),
    path("login/", views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("about_us/", views.about_usPage, name="about_us"),
    path("contact_us/", views.contact_usPage, name="contact_us"),
    path("userProfile/", views.userProfile, name="userProfile"),
    path("create_account/", views.create_account, name="create_account"),
    path("create_opportunity/", views.create_opportunity, name="create_opportunity"),

    #path('create_opportunity/<str:pk>/', views.createOpportunity, name="create_opportunity"),
    #path('update_opportunity/<str:pk>/', views.updateOpportunity, name="update_opportunity"),
    #path('delete_opportunity/<str:pk>/', views.deleteOpportunity, name="delete_opportunity")
]


