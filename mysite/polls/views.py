from django.shortcuts import render
from .models import info
# Create your views here.
def index(request):
    return  render(request,'index.html')
def detail(request):
    getUserName = request.GET.get('detail')
    getPhone = request.GET.get('phone')
    getMessage = request.GET.get('info')
    q1 = info(username=getUserName,phone=getPhone,info=getMessage)
    q1.save()
    return render(request, 'detail.html')
def profile(request):
    return render(request,'profile.html')