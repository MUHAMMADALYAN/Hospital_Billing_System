
from django.shortcuts import render, redirect


# Create your views here.
from module1.form import *
from module1.models import Sale, item


def home(request):


    if request.method == 'POST':
        product(request)
        return redirect('/')
    else:

        dic = item_report()
        context = {'dic': dic}
        return render(request,'home.html',context)

def contact(request):
    return render(request,'contact.html')

def reports(request):
    return render(request,'reports.html')

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
    #each row is object and when we use .all it makes a list of objects or rows
    #The line, first_car_object= Car.objects.first() gets the first object from the Car database.
    #So, if we have 3 cars in our database, Car 1, Car 2, and Car 3, all these will be stored in the all_objects variable.
    for obj in allsales:
        total=total+ obj.price
    allclients = client.objects.all()
    allitems=item.objects.all()
    context = {'allsales': allsales,'total':total ,'allclients' : allclients,'allitems':allitems}
    return render(request, 'datas', context)


# this fun will get all medicines name stored in the database and display in medicine entry module
# here we have used set() in order to avoid duplicate value an then convert it into dictonary to move into html page
def item_report():
    io = item.objects.all()
    st = set()
    for i in io:
        it=i.Item
        st.add(it)
    dic = dict.fromkeys(st)
    return dic













