from django.conf.urls import url,re_path
from . import views
app_name = 'coupons'
urlpatterns = [
 re_path(r'^apply/$', views.coupon_apply, name='apply'),
]
