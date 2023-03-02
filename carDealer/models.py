from django.db import models
from django.utils.timezone import now

class register(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Item(models.Model):
    name=models.CharField(max_length=25)
    profile=models.ImageField(upload_to='pics', blank=True, null=True)
    make = models.CharField(max_length=25, blank=True, null=True)
    year = models.CharField(max_length=25, blank=True, null=True)
    model=models.CharField(max_length=50, blank=True, null=True)
    suspension=models.CharField(max_length=50, blank=True, null=True)
    baseprice=models.IntegerField(blank=True, null=True)
    currentprice=models.IntegerField(blank=True, null=True)
    buyitnow = models.IntegerField(blank=True, null=True)
    status=models.CharField(null=True,max_length=25, blank=True) 
    start_date=models.CharField(max_length=30,blank=True, null=True)
    highest_bidder=models.IntegerField(null=True)
    


    def __str__(self):  
        return self.caption 

class BidDetails(models.Model):
    name=models.CharField(max_length=25)
    baseprice=models.IntegerField()
    currentprice=models.IntegerField()
    make = models.CharField(max_length=25)
    model= models.CharField(max_length=25)
   
class makedetails(models.Model):
    make=models.CharField(max_length=25)
    url=models.CharField(max_length=100)
    urlresized=models.CharField(max_length=100)
   

class admin_register(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

# class UploadImage(models.Model):  
#     caption = models.CharField(max_length=200) 
#     caption1 = models.CharField(max_length=200) 
#     caption2 = models.CharField(max_length=200) 
#     caption3 = models.CharField(max_length=200)  
#     image = models.ImageField(upload_to='images')  
  
#     def __str__(self):  
#         return self.caption  