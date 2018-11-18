"""Lab4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from testApp.views import function_view, ExampleClassBased, ExampleView, tags, OrdersView, OrderView, link

urlpatterns = [
    #path('admin/', admin.site.urls),
    #rl(r'^function_view/', function_view),
    #url(r'^class_based_view', ExampleClassBased.as_view()),
    #url(r'^example', ExampleView.as_view()),
    #url(r'^tags/', tags),
    url(r'^MyGarden/', OrdersView.as_view(), name='garden'),
    url(r'^order/(?P<id>\d+)', OrderView.as_view(), name='order_url'),
    url(r'^link/', link, name='link_url'),
]
