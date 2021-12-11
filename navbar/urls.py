from django.conf import settings
from django.urls import path

from .views import background_View, navbar_View,update_navbar_View,review_View,why_metro_View
from .views import service_View,getintouch_View,footer_View
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns=[
     path('nav-items/', navbar_View),
     path('nav-items/<int:pk>/', update_navbar_View),
     path('background-item/',background_View),
     path('services/', service_View),
      path('reviews/', review_View),
     path('why-metro/', why_metro_View),
      path('get-in-touch-items/', getintouch_View),
       path('footer-items/', footer_View),
     
     
     
]