from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<h2>코스토랑 오픈!</h2>")
    return render(request, 'menus/index.html')
    # return render(request, 'foods/index.html')