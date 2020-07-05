from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
import json
import random
import string

# Create your views here.
from .models import Urls
from .forms import UrlsForm

site_name = 'localhost:8000'
url = None


def home(request):
    global url
    form = UrlsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = Urls.objects.filter(
                original_url=form.cleaned_data['original_url']
            ).first()
            if obj:
                messages.error(request, "URL already shortened!")
                form.cleaned_data['original_url'] = obj.original_url
                form.cleaned_data['shortened_url'] = obj.shortened_url
            else:
                obj = Urls.objects.create(
                    original_url=form.cleaned_data['original_url'],
                    shortened_url=''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(7))
                )
                obj.save()
            url = json.dumps(f'{site_name}/{obj.shortened_url}')
    context = {
        'form': form,
        'url': url
    }
    return render(request, 'home.html', context)


def redirect_to_original_url(request, shortened_url=None):
    link = get_object_or_404(Urls, shortened_url=shortened_url)
    original = link.original_url
    return redirect(original)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'about.html', {})
