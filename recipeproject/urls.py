"""
URL configuration for recipeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from recipeapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("recipedetails/<int:id>", recipedetails),
    path("search", search),
    path("signup", signup),
    path("registeruser",registeruser),
    path("signin", signin),
    path("logout",logout),
    path("contact", contact),
    path("recipeslist", recipeslist),
    path("recipesbytag/<str:tag>",recipesbytag),
    path("verifyuser", verifyuser),
    path("storecontact", storecontact),
    path("searchresults", searchresults),
    path("add_to_wishlist/<int:id>",add_to_wishlist),
    path("wishlist", wishlist),
    path("removeItem/<int:id>", removeItem)
]

