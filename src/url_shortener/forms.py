from django import forms

from .models import Urls


class UrlsForm(forms.ModelForm):
    class Meta:
        model = Urls
        fields = ['original_url']
        widgets = {
            'original_url': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Shorten your link',
                }
            ),
        }
