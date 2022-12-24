from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView

# Create your views here.

def index(request):
  item_list = Item.objects.all()
  context = {
    'item_list':item_list,
  }
  return render(request,'edibles/index.html', context)

class IndexClassView(ListView):
  model = Item;
  template_name = 'edibles/index.html'
  context_object_name = 'item_list'

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

def create_item(request):
  form = ItemForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect('edibles:index')

  return render(request, 'edibles/item-form.html', {'form':form})

def update_item(request, id):
  item = item.objects.get(id=id)
  form = ItemForm(request.POST or None, instance=item)

  if form.is_valid():
    form.save()
    return redirect('edibles:index')

  return render(request, 'edibles/item-form.html', {'form':form, 'item':item})

def delete_item(request, id):
  item = Item.objects.get(id=id)

  if request.method == 'POST':
    item.delete()
    return redirect('edibles:index')

  return render(request, 'edibles/item-delete.html', {'item':item})