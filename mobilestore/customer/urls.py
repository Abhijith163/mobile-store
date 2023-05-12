from django.urls import path
from .views import*
from . import views
from .views import search

urlpatterns = [
    path('chm/',Chome.as_view(),name="chm"),
    path('myo/',views.myorders,name="myod"),
    path('myo/submit-review',views.submit_review,name="review"),
    path('cart/',cart, name='cart'),
    path('cprof/',Cpro.as_view(),name="cprof"),
    path('chm/search',views.search, name='search'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-item/<int:item_id>/', remove_item, name='remove_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/complete_checkout/', views.complete_checkout, name='complete_checkout'),
    
]
