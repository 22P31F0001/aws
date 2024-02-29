from django.shortcuts import render
from . models import Bikeorders
# Create your views here.
def Home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def index(request):
    return render(request,'index.html')
def royal(request):
    return render(request,'royal.html')
def pulsar(request):
    return render(request,'pulsar.html')
def hunter350(request):
    return render(request,'hunter350.html')
def hondadio(request):
    return render(request,'hondadio.html')
def yamaha(request):
    return render(request,'yamaha.html')
def RX(request):
    return render(request,'RX.html')
def orders(request):
    if request.method=="POST":
       Bike_name=request.POST['Bike_name']
       color=request.POST['color']
       cus_name = request.POST['cus_name']
       email=request.POST['email']
       phone=request.POST['phone']
       inst= Bikeorders(Bike_name,color,cus_name,email,phone)
       inst.save()
    return render(request, 'orders.html')
def show_orders(request):
    data=Bikeorders.objects.all()
    return render(request, 'show_orders.html', {'data':data})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def tvs(request):
    return render(request,'tvs.html')
def ktm(request):
    return render(request,'ktm.html')


