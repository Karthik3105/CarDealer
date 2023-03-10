from http.client import HTTPResponse
import os
from django.shortcuts import render
# from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import register, Item, BidDetails, admin_register
from carDealer.models import Item, makedetails
import logging
from django.core.mail import send_mail  
from django.core import serializers
from .forms import UserImage 
from datatableview.views import DatatableView
from datatableview import Datatable
from django.http import HttpResponseRedirect

class ZeroConfigurationDatatableView(DatatableView):
    model = Item

class MyDatatable(Datatable):
    class Meta:
        columns = ["name", "address", "salary", "status"]
        search_fields = ["name", "address"]


class MyView(DatatableView):
    template_name = 'viewvehicle.html'
    model = Item
    datatable_class = MyDatatable

def login(request):
    #  return render(request, "home.html")
      showAll = Item.objects.all()
      return render(request, "login.html", {"items": showAll})

def admin_login(request):
    #  return render(request, "home.html")
      showAll = Item.objects.all()
      return render(request, "admin_login.html", {"items": showAll})
      
def register1(request):
    # return render(request, "register.html")
    if request.method == 'POST':
        register2 = register(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        register2.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def biditem(request):
    id=request.GET['id']
    print(id)
    item = Item.objects.get(id=id)
    # lstatus="live"

    # if item.status ==lstatus:
    return render(request,"biditem.html",{'item':item})
    # else:
    #     return redirect("home")

def validate1(request):
    
     currentprice = request.GET.get('bidrs')
     username1 = request.GET.get('username1')
     iid = request.GET.get('iid')
     make = request.GET.get('make')
     model = request.GET.get('model')
     baseprice = request.GET.get('baseprice')

    # print (iid)

     bidder = request.user
    #  id = Item.objects.get(id=bidder)
    #  bidderEmail = bidder.email
    # print (bidder.id)
     

     mail = "karthikgg9901@gmail.com"
     subject = "Online Bidding"  
    #  msg     = "Congratulations your item is bidded by "
     msg     = "Congratulations "+ make + "item is bidded by " + username1 + " for " + currentprice + "$"
     to      = mail  
     res     = send_mail(subject, msg, "bidmafia007@gmail.com", [to])

     biddetails = BidDetails(bidder.id,'karthik',baseprice,currentprice,make,model)
     biddetails.save()
     

     Item.objects.filter(id=iid).update(currentprice=currentprice)
     Item.objects.filter(id=iid).update(name=username1)
     item_obj = Item.objects.get(id=iid)
    #  if request.method == 'POST':
     return render(request, 'single-list.html',{'item':item_obj})
     return redirect("single-list")
    #  itemownerEmail = item_obj.ownermail

    #  if bidderEmail==itemownerEmail:
    #     return render(request,"notification.html")
    #  else:
    #     mail = item_obj.ownermail
    #     subject = "Online Bidding"  
    #     msg     = "Congratulations your item is bidded by "+bidder.email+", By INR rs = "+value+". Contact your buyer by email Thank You for using our app."
    #     to      = mail  
    #     res     = send_mail(subject, msg, "bidmafia007@gmail.com", [to])
    
     
def index(request):
         
          id1=request.GET['id1']
        #   logging.debug(request)
        #   id1=2
       
          if id1 is "2":
           return render(request, 'index.html')
          elif register.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            register2 = register.objects.get(username=request.POST['username'], password=request.POST['password'])           
            request.session['user_name'] = register2.username
            user_name = request.session['user_name']
            # showAll = Item.objects.all()
            showAll = Item.objects.filter(status='disabled')
            items1 = serializers.serialize("json", showAll)
            return render(request, 'index.html', {"items": showAll, "register2":register2, "user_name":user_name ,"data":items1})
          else:
            # context = {'msg': 'Invalid username or password'}
            messages.success(request, 'Invalid username or password')
            return render(request, 'login.html')
     
def index1(request):
         if request.method == 'POST':
            
          if admin_register.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            admin_register2 = admin_register.objects.get(username=request.POST['username'], password=request.POST['password'])
            showAll = Item.objects.all()
            return render(request, 'index.html', {"items": showAll})
          else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'admin_login.html', context)
def about(request):
     return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def listing_right(request):
    return render(request, "listing-right.html")
def listing_left(request):
    return render(request, "listing-left.html")
def listing_grid(request):
    return render(request, "listing-grid.html")
def single_list(request):
    id=request.GET['id']
    make=request.GET['make']
   
    # request.session.set_expiry(120)
    # username=request.GET['name']
    print(id)
    item = Item.objects.get(id=id)
    # lstatus="Live"
    user_name = request.session['user_name']
    make1 = makedetails.objects.filter(make=make)

    # if item.status ==lstatus:
    return render(request,"single-list.html",{'item':item, 'make' : make1, 'user_name': user_name})
    # else:
    #     return redirect("home")
    # return render(request, "single-list.html")
def blog_right(request):
    return render(request, "blog-right.html")
def blog_grid(request):
    return render(request, "blog-grid.html")
def grid_right(request):
    return render(request, "grid-right.html")
def single_blog(request):
    return render(request, "single-blog.html")
def contact(request):
    return render(request, "contact.html")
def dashboard(request):
    # showAll = Item.objects.all()
    showAll = Item.objects.filter(status='disabled')
    return render(request, "dashboard.html", {"items": showAll})

def addvehicle(request):
    id1=request.GET['id1']
    if id1 is "1":
           return render(request, 'addvehicle.html')
    if request.method == 'POST':  
       items2 = Item(make=request.POST['make'], profile=request.FILES['profile'], model=request.POST['model'], year=request.POST['year']
       ,suspension=request.POST['suspension'],status=request.POST['status'],baseprice=request.POST['baseprice'],
       buyitnow=request.POST['buynow'], start_date=request.POST['bidenddate'])  
                
       items2.save()
       return render(request, "addvehicle.html")
    else:  
       return render(request, "addvehicle.html")

def addvehicle1(request):
         
          
          if admin_register.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            register2 = admin_register.objects.get(username=request.POST['username'], password=request.POST['password'])           
           
            # showAll = Item.objects.all()
          
            return render(request, 'addvehicle.html')
          else:
            # context = {'msg': 'Invalid username or password'}
            messages.success(request, 'Invalid username or password')
            return render(request, 'admin_login.html')

def updatevehicle(request, id):
      if request.method == 'POST':  
        items2 = Item(make=request.POST['make'], profile=request.FILES['profile'], model=request.POST['model'], year=request.POST['year']
       ,suspension=request.POST['suspension'],status=request.POST['status'],baseprice=request.POST['baseprice'],
        buyitnow=request.POST['buynow'], start_date=request.POST['bidenddate']) 

        Item.objects.filter(id=id).update(make=items2.make) 
        # Item.objects.filter(id=id).update(profile='pics/'+items2.profile) 
        Item.objects.filter(id=id).update(model=items2.model) 
        Item.objects.filter(id=id).update(suspension=items2.suspension) 
        Item.objects.filter(id=id).update(status=items2.status) 
        Item.objects.filter(id=id).update(baseprice=items2.baseprice) 
        Item.objects.filter(id=id).update(buyitnow=items2.buyitnow) 
        Item.objects.filter(id=id).update(start_date=items2.start_date)

        post = Item.objects.get(id=id)
        post.profile = request.FILES['profile']
        post.save()
        return render(request, "addvehicle.html", {"item": items2})
        # updateitem = Item.objects.get(id=id)
        # form = UserImage(request.POST, instance=updateitem)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, "Record updated successfully")
        #     return render(request, "addvehicle.html", {"item": updateitem})
        # else:
        #  return render(request, 'addvehicle.html')
def date(request):
    if request.method == 'POST':
        item = Item.objects.get()
        item.start_date =  request.POST['date']
        item.save()
        message = 'update successful'
    return HttpResponseRedirect(request.path_info)

def updatestatus(request, id):
  showAll = Item.objects.all()
  Item.objects.filter(id=id).update(status='disabled')
  items1 = serializers.serialize("json", showAll)
  return render(request, "viewvehicle.html", {"items": showAll, "data":items1})


def viewbids(request):
  showAll = BidDetails.objects.all()
  
  return render(request, "viewbiddingdetails.html", {"bids": showAll})

def payments(request,amount):
    # amount1 = serializers.serialize("json", amount)
    return render(request, 'payments.html', {"amount": amount})

def editvehicle(request,id):
    item1 = Item.objects.get(id=id)
    return render(request, "addvehicle.html", {"item": item1})
def viewvehicle(request):
    showAll = Item.objects.all()
    items1 = serializers.serialize("json", showAll)
    return render(request, "viewvehicle.html", {"items": showAll, "data": items1})
def sample1(request):
    showAll = Item.objects.all()
    return render(request, "sample1.html", {"items": showAll})
def image_request(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'imageform.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImage()  
  
    return render(request, 'imageform.html', {'form': form})  
# def login(request):
#     if request.method == 'POST':
#         if register.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
#             register = register.objects.get(username=request.POST['username'], password=request.POST['password'])
#             return render(request, 'home.html', {'register': register})
#         else:
#             context = {'msg': 'Invalid username or password'}
#             return render(request, 'login.html', context)