from django.shortcuts import render

from module1.models import *

def client_form(request):
    n = request.POST['name']
    ad = request.POST['Address']
    p = request.POST['Phone']
    dis= request.POST['Discount']
    em = request.POST['Email']
    user = client.objects.create(name=n,Adress=ad,Phone=p,Discount=dis,Email=em)
    return user.save()


def item_tax_form(request):
    p = request.POST['party']
    i = request.POST['Item']
    r = request.POST['Rate']
    mp = request.POST['Medicine_Packets']
    tn = request.POST['Tax_Name']
    tr = request.POST['Tax_Rate']
    #saving in model fields item
    user = item.objects.create( party=p,Item=i, Rate=r, Medicine_Packets=mp,Tax_Name=tn, Tax_Rate=tr)
    return user.save()

def product(request):

        # fetching data from html form
        m = request.POST['Medicine']
        qn= request.POST['Quantity']
        pr= request.POST['Price']
        dis = request.POST['Discount']
        user = Sale.objects.create(medicine_name=m,price=pr, discount=dis, quantity=qn)
        return user.save()

