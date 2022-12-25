from django.urls import path
from . import views

# namespacing
app_name = 'edibles'

urlpatterns = [
    # edibles
    path('', views.IndexClassView.as_view(), name='index'),
    path('item/', views.item, name='item'),
    # path('checkout/', views.checkout, name='checkout'),
    path('<int:pk>', views.EdiblesDetail.as_view(), name = 'detail'),
    # add items
    path('add', views.create_item, name='create_item'),
    # edit
    path('update/<int:item_id>', views.update_item, name='update_item' ),
    # delete
    path('delete/<int:id>', views.delete_item, name='delete_item'),
]
