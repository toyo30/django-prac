from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h2>Hellow, Django!</h2>")
    return render(request, 'foods/index.html')