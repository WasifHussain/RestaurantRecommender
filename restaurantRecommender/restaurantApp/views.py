import re
from django.shortcuts import render,redirect
import imp,math
import pandas as pd
from django.http import HttpResponse
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from restaurantApp.ml import get_recommendation_for_restaurant
from .models import Restaurant,Review
from .forms import RestaurantForm,UploadForm,ReviewForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/index')

    return render(request, 'signup.html', {'form': form})

def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/restaurants/page/1')

    return render(request, 'signin.html', {'form': form})
def signout(request):
    logout(request)
    return redirect('/index')

def post_restaurant(request):
    form = RestaurantForm()
    if request.method == "POST":
        restaurant_form = RestaurantForm(request.POST)

        if restaurant_form.is_valid():
            restaurant_form.save()
            return redirect('/restaurants/page/1')
    return render(request, 'post_restaurant.html',{'form':form})

def get_restaurants(request, page_number):
    page_size = 5

    if page_number < 1:
        page_number = 1

    restaurant_count =  Restaurant.objects.count()

    last_page = math.ceil(restaurant_count/page_size)

    pagination = {
        'previous_page': page_number - 1,
        'current_page': page_number,  
        'next_page': page_number + 1,
        'last_page': last_page
    }
    restaurants = Restaurant.objects.all()[(page_number-1)
                                 * page_size:page_number*page_size]
    return render(request,'restaurants.html',{'restaurants':restaurants, 'pagination': pagination})

def add_to_favorite(request, id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.favorite.add(request.user)

    return redirect('/restaurant/{0}'.format(id))

def remove_from_favorites(request, id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.favorite.remove(request.user)

    return redirect('/restaurant/{0}'.format(id))

def get_user_favorites(request):
    restaurants = request.user.favorite.all()
    return render(request, 'user_favorite.html', {'restaurants': restaurants})


def  get_restaurant_info(request, id):
    if not request.user.is_authenticated:
        return redirect('/signin')
    try:
        review_form = ReviewForm()
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.restaurant_id = id
                review.user_id = request.user.id
                review.save()

        restaurant = Restaurant.objects.get(id=id)
        reviews = Review.objects.filter(restaurant=restaurant).order_by('-created_at')[0:4]
        context = {
                'is_favorite': False
        }
        restaurant_ids = get_recommendation_for_restaurant(id)

        recommended_restaurants = Restaurant.objects.filter(id__in=restaurant_ids)

        if restaurant.favorite.filter(pk=request.user.pk).exists():
            context['is_favorite'] = True
        return render(request,"restaurant.html",{'restaurant':restaurant,'context':context,'reviews':reviews,'review_form':review_form,'recommended_restaurants':recommended_restaurants})
    except Restaurant.DoesNotExist:
        return render(request,'404.html')

def upload_dataset(request):
    file_form = UploadForm()
    error_messages = {}

    if request.method == "POST":
        file_form = UploadForm(request.POST, request.FILES)
        try:
            if file_form.is_valid():
                dataset = pd.read_csv(request.FILES['file'])
                new_restaurants_list = []
                with transaction.atomic():
                    for index, row in dataset.iterrows():
                        restaurant = Restaurant(
                            name=row['name'],
                            address=row['address'],
                            city=row['city'],
                            alcohol=row['alcohol'],
                            smoking_area=row['smoking_area'],
                            dresscode=row['dress_code'],
                            accessibility=row['accessibility'],
                            price=row['price'],
                            ambience=row['Rambience'],
                            area=row['area'],
                            other_services=row['other_services'],
                        )

                        new_restaurants_list.append(restaurant)

                Restaurant.objects.bulk_create(new_restaurants_list)
                return redirect('restaurants/page/{0}'.format(id))
        except Exception as e:
            error_messages['error'] = e

    return render(request, 'upload_dataset.html', {'form': file_form, 'error_messages': error_messages})

