from django.db import IntegrityError
import sys
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Food.models import *

# Create your views here.
def home(request):
    return render(request,'home.html')


def SignUp(request):
    if request.method=='POST':
        try:
            pn=request.POST['Name']
            pe=request.POST['email']
            db=request.POST['DOB']
            pp=request.POST['pswd']
            pu=ProjectUser(Name=pn,Email=pe,Password=pp,DOB=db)
            pu.save()
            return redirect('/Food/login')
        except Exception as e:
            return HttpResponse(e)
    return render(request,'SignUp.html')

def LogIn(request):
    if request.method=='POST':
        try:
            em=request.POST['email']
            ps=request.POST['pswd']
            P=ProjectUser.objects.get(Email=em,Password=ps)
            request.session['USER']=P.Name
            return redirect('/Food/help2')
        except Exception as e:
            return redirect('/Food/login')
    return render(request,'LogIn.html')

def about(request):
    if 'USER' in request.session.keys():
        return render(request,'about.html')
    return redirect('/Food/login')

def contact(request):
    return render(request,'contact.html')


def logout(request):
    if 'USER' in request.session.keys():
        del request.session['USER']
        return redirect('/Food/home')
    else:
        return redirect('/Food/home')


def help2(request):
    return render(request,'help2.html')


#def view_orders(request):
    #if request.user.is_superuser:
        #make a request for all the orders in the database
        #rows = UserOrder.objects.all().order_by('-time_of_order')
        #orders.append(row.order[1:-1].split(","))

       # return render(request, "order/order.html", context = {"rows":rows})
    #else:
        #rows = UserOrder.objects.all().filter(username = request.user.username).order_by('-time_of_order')
        #return render(request, "order/order.html", context = {"rows":rows})
