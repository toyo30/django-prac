from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    today = datetime.now().date()
    context = {'today': today}
    # return HttpResponse("<h2>코스토랑 오픈!</h2>")
    return render(request, 'menus/index.html', context)
    # return render(request, 'foods/index.html')


def detail(request, menu):
    context = dict()
    # if menu == ""
    return render(request, 'menus/detail.html', context=context)