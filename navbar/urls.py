from django.urls import path
from .views import navbar_View
urlpatterns=[
     path('nav-items/', navbar_View),
]