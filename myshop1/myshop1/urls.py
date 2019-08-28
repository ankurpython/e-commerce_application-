"""myshop1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
#from shop import views as shop
#from orders import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('cart', include('cart.urls')),
    #path('orders/', include('orders.urls')),
    re_path(r'^coupons/', include('coupons.urls', namespace='coupons')),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls', namespace='cart')),
    re_path(r'^orders/', include('orders.urls', namespace='orders')),
    re_path(r'^paypal/', include('paypal.standard.ipn.urls')),
    re_path(r'^payment/', include('payment.urls', namespace='payment')),
    #re_path(r'^accounts/', include('django.contrib.auth.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
