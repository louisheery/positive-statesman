from django.shortcuts import render


def index(request, path=None):
    print(path)
    return render(request, 'frontend/index.html')
