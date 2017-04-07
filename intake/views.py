from django.shortcuts import render

def index(request):
    context = {'message': 'randy..............thank you'}
    return render(request, 'intake/index.html', context)
