from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from module1.form import *
from module1.models import Sale, item


def home(request):
    if request.method == 'POST':
        product(request)
        return redirect('/')
    else:
        return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')




def masters(request):
    if request.method == 'POST':
        if "client_form" in request.POST:
            client_form(request)
        elif "item_form" in request.POST:
            # fetching data from html form
            item_tax_form(request)
        #/ must be in start for redirect
        return redirect('/')

    else:
        return render(request,'masters')

def datas(request):
    total=0
    allsales = Sale.objects.all()
    for obj in allsales:
        total=total+ obj.price
    allclients = client.objects.all()
    allitems=item.objects.all()



    context = {'allsales': allsales,'total':total ,'allclients' : allclients,'allitems':allitems}
    return render(request, 'datas', context)

