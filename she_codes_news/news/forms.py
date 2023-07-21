from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        # delete author here, as login user is the author
        # fields =['title','author','pub_date','content']
        fields =['title','image_url','pub_date','content','category']
        widgets = {
            'pub_date':forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            )
        }
