from django import forms
from apps.gallery.models import Photo

class PhotoForms(forms.ModelForm): # we use ModelForm to create a form based on a model
    class Meta:
        model = Photo
        exclude = ['published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),           
        }