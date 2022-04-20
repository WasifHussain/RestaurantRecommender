from django import forms
from .models import Restaurant, Review
class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name','address','city','alcohol','smoking_area','dresscode','accessibility','price','ambience','area','other_services']
class UploadForm(forms.Form):
    file  = forms.FileField()
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']