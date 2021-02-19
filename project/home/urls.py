from django.contrib import admin
from django.urls import path, include 
from . import views
# imported to access static files
from django.conf.urls.static import static
# imported to access setting function
from django.conf import settings
urlpatterns = [
	path('', views.home, name="home"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
