from django.shortcuts import render
import json
 
def dashboard(request):
    context          = {}
    context['hello'] = 'Hello World!'
    with open('statics/data/texture_dict.json') as f:
        texture_dict = json.load(f)
    with open('statics/data/feature_dict.json') as f:
        feature_dict = json.load(f)
    context['texture_dict'] = texture_dict
    context.update(feature_dict)
    return render(request, 'index.html', context)

def products(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'products.html', context)

def accounts(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'accounts.html', context)

def login(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)