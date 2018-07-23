from django.shortcuts import render


def index(request):
    if request.methods == 'GET':
        return render(request, 'index.html')


