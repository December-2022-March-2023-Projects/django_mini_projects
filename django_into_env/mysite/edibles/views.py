from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.

def index(request):
  item_list = Item.objects.all()
  context = {
    'item_list':item_list,
  }
  return render(request,'edibles/index.html', context)

def item(request):
  return HttpResponse('This is my test item')

def checkout(request):
  html = "<html><body><h1>Checkout here</body></h1></html>"
  return HttpResponse(html)

def detail(request, item_id):
  item = Item.objects.get(pk=item_id)
  context = {
    'item':item,
  }
  return render(request, 'edibles/detail.html', context)