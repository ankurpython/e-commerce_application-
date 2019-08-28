from django.conf.urls import url,re_path,include
from . import views

app_name = 'orders'

urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
    re_path(r'^admin/order/(?P<order_id>\d+)/$',views.admin_order_detail,name='admin_order_detail'),
    #re_path(r'^login/$','django.contrib.auth.views.login',name='login'),
    #re_path(r'^logout/$','django.contrib.auth.views.logout',name='logout'),
    #re_path(r'^logout-then-login/$','django.contrib.auth.views.logout_then_login',name='logout_then_login'),
    #re_path(r'^accounts/', include('django.contrib.auth.urls')),
    #re_path(r'^logout/',views.logout_view),
    re_path(r'^logout/$',views.logout_view),
    re_path(r'^signup/$',views.signup_view),
]
