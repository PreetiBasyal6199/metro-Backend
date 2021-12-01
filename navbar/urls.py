from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import navbar_View,update_navbar_View

from . import views
urlpatterns=[
     path('nav-items/', navbar_View),
     path('nav-items/<int:pk>/', update_navbar_View),
     path('background-item/', views.background_View),
     
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)