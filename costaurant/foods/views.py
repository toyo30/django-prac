from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse("<h2>Hellow, Django!</h2>")
    today = datetime.today().date()
    #render 함수. 첫번째 변수 호출 방법, 2번째 변수 호출 값 3번째 변수 데이터
    context = {"date":today}
    return render(request, 'foods/index.html', context=context)