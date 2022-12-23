from django.urls import path
from . import views

# namespacing
app_name = 'edibles'

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('checkout/', views.checkout, name='checkout'),
    path('<int:item_id>', views.detail, name = 'detail'),
    # add items
    path('add', views.create_item, name='create_item'),
    # edit
    path('update/<int:item_id>', views.update_item, name='update_item' ),
]
