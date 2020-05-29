from django.shortcuts import render
import json
 
def dashboard(request):
    context          = {}
    context['hello'] = 'Hello World!'
    with open('statics/data/texture_dict.json') as f:
        texture_dict = json.load(f)
    with open('statics/data/feature_dict.json') as f:
        feature_dict = json.load(f)
    with open('statics/data/line_dict.json') as f:
        line_dict = json.load(f)
    with open('statics/data/pie_dict.json') as f:
        pie_dict = json.load(f)
    context['texture_dict'] = texture_dict
    context.update(feature_dict)
    context.update(line_dict)
    context.update(pie_dict)
    return render(request, 'index.html', context)

def products(request):
    context          = {}
    context['hello'] = 'Hello World!'
    with open('statics/data/pred_dict.json') as f:
        pred_dict = json.load(f)
    with open('statics/data/feature_dict.json') as f:
        feature_dict = json.load(f)
    context.update(pred_dict)
    context.update(feature_dict)
    return render(request, 'products.html', context)

def accounts(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'accounts.html', context)

def login(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)