#copied urls.py from the chatbot (project) directory into the home (app) directory

"""
URL configuration for chatbot project.

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
from home.views import chat, chatAPI

urlpatterns = [
    #first param is name of endpoint
    #second param is name of (imported) function 
    #third param is just a name for the url
    
    path('', chat, name='home'),  #whenever we reach homepage (empty url), include all the urls of the "home" app
    path('api', chatAPI, name='chatAPI'),
]