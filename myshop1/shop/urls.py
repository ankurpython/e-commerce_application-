#from django.conf.urls import url,re_path,path
from django.urls import path,include,re_path

from shop import views
app_name='shop'
urlpatterns = [
 path('index', views.index),
 re_path(r'^$', views.product_list, name='product_list'),
 re_path(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
 re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),
 #path('<int:id>/<slug:slug>/',views.product_detail, name='product_detail'),
]
