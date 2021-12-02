from django.conf import settings
from django.urls import path

from .views import background_View, navbar_View,update_navbar_View,service_View,why_metro_View


from . import views
urlpatterns=[
     path('nav-items/', navbar_View),
     path('nav-items/<int:pk>/', update_navbar_View),
     path('background-item/',background_View.as_view()),
     path('services/', service_View.as_view()),
     path('why-metro/', why_metro_View),
     
]