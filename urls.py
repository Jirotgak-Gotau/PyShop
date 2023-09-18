from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('pyshop.urls')),
    path('authapp/', include('authapp.urls')), # Replace 'yourapp' with your app's name
]
