from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('checkout/', views.checkout, name='checkout'),
    path('<int:item_id>', views.detail, name = 'detail'),
]
