"""Subscription URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Subscrap import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
# Landing Pages
    path('admin/', admin.site.urls),
    path('', views.home),
    path ('main/', views.main),


# Registration Pages

    path('login/', views.login),
    path('signup/', views.registration),
    path ('logout/', views.Log_out),

# Data Manipulation Pages

    path ('addnew/', views.addnew),
    path ('editprofile/', views.edituserprofile, name = 'Edit_Profile'),
    path ('accountsettings/', views.useraccountsettings, name = 'Account_Settings'),
    path ('editsubscription/<int:id>', views.editusersub, name = 'Edit_Sub'),
    path('addpresavedsub/<int:id>', views.addpresavedsubscription),
    path('deletelist/<int:id>', views.deletelist),

# Searching Pages

    path ('search_user_sublist', csrf_exempt(views.search_user_sublist), name = "Search_Sublist"),
    path ('search/', views.search_results,name='search'),
    path('ajax/', views.ajaxview), #not using this

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



