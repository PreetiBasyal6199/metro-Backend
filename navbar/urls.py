from django.urls import path
from .views import navbar_View,update_navbar_View
from . import views
urlpatterns=[
     path('nav-items/', navbar_View),
     path('nav-items/<int:pk>/', update_navbar_View),
     path('background-items/', views.background_View),

]