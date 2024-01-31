

# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('app1.urls')),
    path('', views.index),
]
