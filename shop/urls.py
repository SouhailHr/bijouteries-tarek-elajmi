"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from product import urls as urls_product
from product.views import all_products
from django.views import static
from .settings import MEDIA_ROOT
from home.views import home
from home import urls as urls_home

urlpatterns = [
    path('', home, name='home'),
    path('home/', include(urls_home)),
    path('admin/', admin.site.urls),
    path('product/', include(urls_product)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})

]
