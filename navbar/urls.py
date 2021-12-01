from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import navbar_View,update_navbar_View
from .views import background_view
from . import views
urlpatterns=[
     path('nav-items/', navbar_View),
     path('nav-items/<int:pk>/', update_navbar_View),
     path('background-item/', views.background_View),
     path('background-items/',background_view.as_view() ),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)