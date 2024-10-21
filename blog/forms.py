from django.forms import ModelForm
from django import forms
from .models import Blog_review

class Review(ModelForm):
    class Meta:
        model = Blog_review
        fields = ['username','email','review_text']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input_mamamiya',  
                'placeholder': 'نام*',  
            }),
            'email': forms.TextInput(attrs={
                'class': 'input_mamamiya',  
                'placeholder': 'ایمیل*',  
            }),
            'review_text': forms.TextInput(attrs={
                'class': 'input_mama ',  
                'placeholder': 'دیدگاه',  
                'cols': "30",
                'rows': "10"
            }),
        }