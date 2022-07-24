from ast import operator
import collections
from math import prod
from typing import OrderedDict
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import application, product, connecting
from django.db import connection
from collections import defaultdict

# Create your views here.
def list_all_items(request:HttpRequest):
    
    # data = {}
    # pn = product.objects.values_list('pid')
    # for x in pn:
    #     product_application = connecting.objects.filter(product_id = x[0]).values_list('application_id')
    #     data[x[0]] = product_application
    # print(data)
    
    # for a, b in data.items():
    #     mylist = []
    #     for i in b:
    #         mylist.append(i[0])
    #         data[a] = mylist
    # print(data)

    temp = {}
    pnames = product.objects.values_list('pid', 'name')
    for x in pnames:
        # print(x[0])
        product_application = connecting.objects.filter(product_id = x[0]).values_list('application_id', flat=True)
        temp[x[1]] = product_application
    # print(temp)

    for a, b in temp.items():
        mylist = []
        for i in b:
            anames = application.objects.filter(aid = i).values_list('name', flat=True)
            mylist.append(anames[0])
            temp[a] = mylist
    print(temp)
    
    context = {
        'data' : temp
    }


    return render(
        request,
        'company/list_items.html',
        context
    )


def insert_Items(request:HttpRequest):
    product_item = product(
        id = request.POST['SimplePID'],
        pid = request.POST['ProductID'],
        name = request.POST['ProductName'],
        description = request.POST['ProductDesc'],
        source_url = request.POST['ProductURL'],
    )
    
    application_item = application(
        id = request.POST['SimpleAID'],
        aid = request.POST['ApplicationID'],
        name = request.POST['ApplicationName'],
        description = request.POST['ApplicationDesc'],
        source_url = request.POST['ApplicationURL']
    )

    product_item.save()
    application_item.save()

    data1 = request.POST['SimplePID']
    product_obj = product.objects.get(id = data1)
    data2 = request.POST['SimpleAID']
    application_obj = application.objects.get(id = data2)
    connecting.objects.create(
        product_id = product_obj.pid,
        application_id = application_obj.aid
    )

    

    return redirect('/company/list/')
