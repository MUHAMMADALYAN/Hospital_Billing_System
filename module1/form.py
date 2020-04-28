from django.shortcuts import render

from module1.models import *

def client_form(request):
    n = request.POST['name']
    ad = request.POST['Address']
    p = request.POST['Phone']
    em = request.POST['Email']
    user = Client.objects.create(name=n,Adress=ad,Phone=p,Email=em)
    return user.save()


def item_tax_form(request):
    p = request.POST['party']
    i = request.POST['Item']
    r = request.POST['Rate']
    mp = request.POST['Medicine_Packets']
    tn = request.POST['Tax_Name']
    tr = request.POST['Tax_Rate']
    tr=int('0'+tr)
    #saving in model fields item
    user = Item.objects.create( party=p,Item=i, Rate=r, Medicine_Packets=mp,Tax_Name=tn, Tax_Rate=tr)
    return user.save()

def product(request):

        # fetching data from html form
        m = request.POST['Medicine']
        qn= request.POST['Quantity']
        pr= request.POST['Price']
        dis = request.POST['Discount']
        dis = int('0' + dis)
        user = Sale.objects.create(medicine_name=m,price=pr, discount=dis, quantity=qn)
        return user.save()





