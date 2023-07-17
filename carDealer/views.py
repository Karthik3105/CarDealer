from http.client import HTTPResponse
import os

from django.shortcuts import render
# from .forms import UserRegistrationForm
from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User, auth
from django.template import RequestContext


from .models import register, Item, BidDetails, admin_register
from carDealer.models import Item, makedetails, ItemImage
from carDealer.serializers import ItemSerializers
import logging
from django.core.mail import send_mail  
from django.core import serializers
from .forms import UserImage 
from datatableview.views import DatatableView
from datatableview import Datatable
from django.http import HttpResponseRedirect
# import boto
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from authorizenet import apicontractsv1
from authorizenet.apicontractsv1 import *
from authorizenet.apicontrollers import createTransactionController
from . import settings
# from boto.s3.key import Key

LOCAL_PATH = '/backup/s3/'
AWS_ACCESS_KEY_ID = 'AKIA3ATMXJJBNYMX7M47'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = 'filestorage-cardealer'



class ImageCreateView(CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ItemSerializers
    #   def post(self,request,*args,**kwargs):
      
    #   return render(request, "login.html", {"items": "k"})

    def post(self, request, format=None):
        serializer = ItemSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return render(request, "addvehicle.html")

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

@csrf_exempt
def login(request):
    #  return render(request, "home.html")
      showAll = Item.objects.all()
      return render(request, "login.html", {"items": showAll})

@csrf_exempt
def password_reset(request):
      
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
         u = User.objects.get(username=username)
         u.set_password(password)
         u.save()
        
         return render(request, "login.html")
        else:
         messages.success(request, 'Invalid username')
         return render(request, "password_reset_form.html")
    else:
        return render(request, "password_reset_form.html")

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('login')

@csrf_exempt
def admin_login(request):
    #  return render(request, "home.html")
      showAll = Item.objects.all()
      return render(request, "admin_login.html", {"items": showAll})

@csrf_exempt
def register3(request):

    if request.method == 'POST':

       
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.create_user(username = username , password = password)
        user1 = User.objects.create_superuser(username='angelinvestor',
        password='seedfunding')
        user.save()
        # user1.save()
        print('user created')
        return redirect('/login')

    return render(request,'register.html')

@csrf_exempt     
def register1(request):
    # return render(request, "register.html")
    if request.method == 'POST':
        register2 = register(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        register2.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
    
@csrf_exempt
def biditem(request):
    id=request.GET['id']
    print(id)
    item = Item.objects.get(id=id)
    # lstatus="live"

    # if item.status ==lstatus:
    return render(request,"biditem.html",{'item':item})
    # else:
    #     return redirect("home")
@csrf_exempt
def mybids(request):
    user_name = request.session['user_name']
    showAll = BidDetails.objects.filter(name=user_name)
    return render(request,"mybids.html",{'showAll':showAll})  
    
@csrf_exempt
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
     res     = send_mail(subject, msg, "karthikgg1995@gmail.com", [to])

     biddetails = BidDetails(bidder.id, username1 ,baseprice,currentprice,make,model)
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
@csrf_exempt   
def index2(request):
    return render(request, 'index.html')

@csrf_exempt
def index3(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request , user)
            
            request.session['user_name'] = username
            user_name = request.session['user_name']
            
            showAll = Item.objects.filter(status='disabled')
            
          
            list_ = []
           
            for i in showAll:
             showAll1 = ItemImage.objects.filter(product_id=i.id).first()
             list_.append(showAll1.image)
          
            
             l = zip(showAll, list_)
            return render (request, 'index.html', {"items": l, "user_name":user_name} )
           
        else:
            messages.info(request, 'invalid username or password')
            return  render (request, 'login.html')
    else:
         username = None
         if request.user.is_authenticated:
            username = request.user.username
            request.session['user_name'] = username
            user_name = request.session['user_name']
            # user_name = request.session['user_name']
            showAll = Item.objects.filter(status='disabled')
            
          
            list_ = []
           
            for i in showAll:
             showAll1 = ItemImage.objects.filter(product_id=i.id).first()
             list_.append(showAll1.image)
          
            
             l = zip(showAll, list_)

            return render(request,'index.html', {"items": l,"user_name":user_name})

@csrf_exempt    
def index(request):
         
          try:
           id1=request.GET['id1']
          except MultiValueDictKeyError:
           id1 = 1 
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

            for fav in showAll:
             print(fav.id)
           
          
            list_ = []
            # showAll1 = ItemImage.objects.all()
            for i in showAll:
             showAll1 = ItemImage.objects.filter(product_id=i.id).first()
             list_.append(showAll1.image)
            #  data = {'devices' : showAll.suspension}
            
             l = zip(showAll, list_)
            
            #  list_.append(showAll1)
            
            # data = {'item' : 'kk', 'device': 'kk', 'log': 'll'}
            # list_.append(data)
            # showAll2 = Item.objects.get(make='Great Dane 10')
            print(list_)
            # items1 = serializers.serialize("json", list_)
            # article = ItemImage.objects.filter(product_id=Item.year)
            # conn = boto.connect_s3('AKIA3ATMXJJBNYMX7M47', 'S5g1CV+ODVBWL+L7cdO5dlsqOMHLkYQ5dtK2emVh')
            # bucket = conn.get_bucket('filestorage-cardealer')
            # s3_file_path = bucket.get_key('/filestorage-cardealer/88/ff/mm_xw44PTW')
            # url = s3_file_path.generate_url(expires_in=600) # expiry time is in seconds
           
            # return HttpResponseRedirect(url)
            return render(request, 'index.html', {"items": l, "register2":register2, "user_name":user_name})
          else:
            # context = {'msg': 'Invalid username or password'}
            messages.success(request, 'Invalid username or password')
            return render(request, 'login.html')
          
@csrf_exempt    
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

@csrf_exempt
def single_list(request):
    id=request.GET['id']
    make=request.GET['make']
   
    # request.session.set_expiry(120)
    # username=request.GET['name']
    # print(id)
    item = Item.objects.get(id=id)
   
    # # lstatus="Live"
  
    
    showAll1 = ItemImage.objects.filter(product_id=id)
    items1 = serializers.serialize("json", showAll1)
    

    user_name = request.session['user_name']
    # make1 = makedetails.objects.filter(make=make)

    # if item.status ==lstatus:
    return render(request,"single-list.html",{ 'item':item, 'showAll1':showAll1, 'make' : item.make, 'user_name': user_name, 'items1':items1})
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

@csrf_exempt
def dashboard(request):
    # showAll = Item.objects.all()
    showAll = Item.objects.filter(status='disabled')
    return render(request, "dashboard.html", {"items": showAll})

@csrf_exempt
def addvehicle(request):
    id1=request.GET['id1']
    if id1 is "1":
           return render(request, 'addvehicle.html')
    if request.method == 'POST':  
    #    file = request.FILES.getlist('profile')
    #    s3 = boto3.resource('s3', aws_access_key_id='AKIA3ATMXJJBNYMX7M47', aws_secret_access_key='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')
    #    bucket = s3.Bucket('filestorage-cardealer')
    #    bucket.put_object(Key='kk', Body=file)
    #    images = request.FILES.getlist('profile')
    #    for image in images:
    #         MultipleImage.objects.create(images=image)
    #    images = MultipleImage.objects.all()
       items2 = Item(make=request.POST['make'], profile=request.FILES['profile'], model=request.POST['model'], year=request.POST['year']
       ,suspension=request.POST['suspension'],status=request.POST['status'],baseprice=request.POST['baseprice'],
       buyitnow=request.POST['buynow'], start_date=request.POST['bidenddate'])  
                
       items2.save()
       return render(request, "addvehicle.html")
    else:  
       return render(request, "addvehicle.html")

@csrf_exempt
def addvehicle1(request):
         
          
          if admin_register.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            register2 = admin_register.objects.get(username=request.POST['username'], password=request.POST['password'])           
           
            # showAll = Item.objects.all()
          
            return render(request, 'addvehicle.html')
          else:
            # context = {'msg': 'Invalid username or password'}
            messages.success(request, 'Invalid username or password')
            return render(request, 'admin_login.html')

@csrf_exempt
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

@csrf_exempt        
def date(request):
    if request.method == 'POST':
        item = Item.objects.get()
        item.start_date =  request.POST['date']
        item.save()
        message = 'update successful'
    return HttpResponseRedirect(request.path_info)

@csrf_exempt
def updatestatus(request, id):
  showAll = Item.objects.all()
  Item.objects.filter(id=id).update(status='disabled')
  items1 = serializers.serialize("json", showAll)
  return render(request, "viewvehicle.html", {"items": showAll, "data":items1})

@csrf_exempt
def viewbids(request):
  showAll = BidDetails.objects.all()
  
  return render(request, "viewbiddingdetails.html", {"bids": showAll})

@csrf_exempt
def payments(request,amount):
    # amount1 = serializers.serialize("json", amount)
    return render(request, 'payments.html', {"amount": amount})

@csrf_exempt
def editvehicle(request,id):
    item1 = Item.objects.get(id=id)
    return render(request, "addvehicle.html", {"item": item1})

@csrf_exempt
def viewvehicle(request):
    showAll = Item.objects.all()
    items1 = serializers.serialize("json", showAll)
    return render(request, "viewvehicle.html", {"items": showAll, "data": items1})

@csrf_exempt
def sample1(request):
    showAll = Item.objects.all()
    return render(request, "sample1.html", {"items": showAll})

@csrf_exempt
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


def payment_view(request):
    if request.method == 'POST':
        # Retrieve payment information from the form
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')

        # Create a transaction request
        transaction = apicontractsv1.transactionRequestType()
        transaction.transactionType = "authCaptureTransaction"
        transaction.amount = "10.00"  # Example amount, adjust as needed

        # Set payment details
        payment = apicontractsv1.paymentType()
        credit_card = apicontractsv1.creditCardType()
        credit_card.cardNumber = card_number
        credit_card.expirationDate = expiration_date
        credit_card.cardCode = cvv
        payment.creditCard = credit_card
        transaction.payment = payment

        # Set billing address
        customer_address = apicontractsv1.customerAddressType()
        customer_address.firstName = first_name
        customer_address.lastName = last_name
        customer_address.address = address
        customer_address.city = city
        customer_address.state = state
        customer_address.zip = zip_code
        transaction.billTo = customer_address

        # Create a request
        create_request = apicontractsv1.createTransactionRequest()
        create_request.merchantAuthentication = apicontractsv1.merchantAuthenticationType()
        create_request.merchantAuthentication.name = settings.AUTHNET_API_LOGIN_ID
        create_request.merchantAuthentication.transactionKey = settings.AUTHNET_TRANSACTION_KEY
        create_request.transactionRequest = transaction

        # Send the request to Authorize.Net API
        controller = createTransactionController(create_request)
        controller.execute()

        # Process the response
        response = controller.getresponse()

        if response.messages.resultCode == "Ok":
            # Payment successful
            return redirect('payment_success')
        else:
            # Payment failed
            # return redirect('login')
            error_message = response.messages.message[0]['text']
            context = {'error_message': error_message}
    else:
        return render(request, 'payment_index.html')          
