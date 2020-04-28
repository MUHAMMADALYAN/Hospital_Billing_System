
from django.shortcuts import render, redirect


# Create your views here.
from module1.form import *
from module1.models import Sale, Item


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
    m=report()
    p,c=medicine_reports()
    context = {'m': m,'p':p,'c':c}
    return render(request,'reports.html',context)

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
    allclients = Client.objects.all()
    allitems=Item.objects.all()
    context = {'allsales': allsales,'total':total ,'allclients' : allclients,'allitems':allitems}
    return render(request, 'datas', context)


# this fun will get all medicines name stored in the database and display in medicine entry module
# here we have used set() in order to avoid duplicate value an then convert it into dictonary to move into html page
def item_report():
    io = Item.objects.all()
    st = set()
    for i in io:
        it=i.Item
        st.add(it)
    dic = dict.fromkeys(st)
    return dic



def report():
    so = Sale.objects.all()
    # initializing list or array
    a=[]
    for i in so:
        it=i.medicine_name
        # adding medicines names in list
        a.append(it)
        #removing duplications using dicitionary
    mylist = list(dict.fromkeys(a))
    return mylist

def medicine_reports():
    tp=[]
    sp=[]
    total_price=0
    sold_packets=0
    medicine_list=report()
    so = Sale.objects.all()
    for m in medicine_list:
        for s in so:
            if m == s.medicine_name:
                total_price=total_price+(s.price)
                sold_packets=sold_packets+(s.quantity)
        tp.append(total_price)
        sp.append(sold_packets)
        total_price = 0
        sold_packets = 0
    return tp,sp











