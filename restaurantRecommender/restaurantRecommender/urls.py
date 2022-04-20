"""restaurantRecommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from restaurantApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('signup/', views.signup, name="User Sign Up"),
    path('signin/', views.signin, name="User Sign In"),
    path('signout/', views.signout, name="User Sign Out"),
    path('post_restaurant/',views.post_restaurant),
    path('restaurants/page/<int:page_number>', views.get_restaurants, name="Restaurants Page"),
    path('upload_dataset/', views.upload_dataset, name="Upload dataset"),
    path('restaurant/<int:id>',views.get_restaurant_info),
    path('user_favorites', views.get_user_favorites),
    path('add_to_favorite/<int:id>', views.add_to_favorite),
    path('remove_from_favorites/<int:id>',views.remove_from_favorites),

]
