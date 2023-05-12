from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reg/',Reg.as_view(),name="register"),
    path('log/',Log.as_view(),name="login"),
    path('logout/',Logout.as_view(),name="logout"),
]

 