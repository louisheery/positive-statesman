from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')

def category(request, path=None):
    return render(request, 'frontend/index.html')
