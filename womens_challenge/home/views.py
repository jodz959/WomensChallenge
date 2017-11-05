from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')


def groups(request):
    return render(request, 'home/groups.html')

def opportunities(request):
    return render(request, 'home/opportunities.html')

def user(request):
    return render(request, 'home/user.html')

def mentor(request):
    return render(request, 'home/mentor.html')
