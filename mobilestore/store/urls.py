from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('strh/',SHome.as_view(),name="sh"),
    path('addm/',add_mob,name="ad"),
    path('prof/',Pro.as_view(),name="prof"),
    path('strh/orders', orders, name="orders"),
    path('edm/<int:pk>',Edit_mob.as_view(),name="em"),
    path('edl./<int:pk>',Delete_mob.as_view(),name="dm"),
    path('edp/<int:pk>',Edit_prof.as_view(),name="ep"),
    path('searchhh',searchhhh, name='search12'),
    
    
]

