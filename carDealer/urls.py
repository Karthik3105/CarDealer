"""carDealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, re_path, include
from django.urls import re_path as urls
from django.conf.urls import url
from . import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [


    url(r'^addvehicle$', views.addvehicle, name='addvehicle'),
    url(r'^addvehicle1$', views.addvehicle1, name='addvehicle1'),
    url(r'^editvehicle/(?P<id>\d+)/$', views.editvehicle, name='editvehicle'),
    path('payments/<int:amount>', views.payments, name='payments'),
    path('admin/', admin.site.urls),
    path('', views.admin_login, name='admin_login'),
    # path('addvehicle', views.addvehicle, name='addvehicle'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('date', views.date, name='date'),
    # path('editvehicle/<int:id>', views.editvehicle, name='editvehicle'),
    path('updatevehicle/<int:id>', views.updatevehicle, name='updatevehicle'),
    path('updatestatus/<int:id>', views.updatestatus, name='updatestatus'),
    url(r'^viewbids/$', views.viewbids, name='viewbids'),
    path('image_request', views.image_request, name = "image-request"), 
    path('login', views.login, name='login'),
    path('register', views.register1, name='register'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('biditem',views.biditem,name="biditem"),
    path('items/biditem',views.biditem,name="biditem"),
    path('validate1',views.validate1,name="validate1"),
    path('index', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    path('about', views.about, name = 'about'),
    path('services', views.services, name = 'services'),
    path('listing-right', views.listing_right, name = 'listing-right'),
    path('listing-left', views.listing_left, name = 'listing-left'),
    path('listing-grid', views.listing_grid, name = 'listing-grid'),
    path('single-list', views.single_list, name = 'single-list'),
    path('blog-right', views.blog_right, name = 'blog-right'),
    path('grid-right', views.grid_right, name = 'grid-right'),
    path('single-blog', views.single_blog, name = 'single-blog'),
    path('contact', views.contact, name = 'contact'),
    path('blog-grid', views.blog_grid, name = 'blog-grid'),
    path('viewvehicle', views.viewvehicle, name = 'viewvehicle'),

]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
urlpatterns = urlpatterns  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)