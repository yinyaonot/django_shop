from django.contrib import admin
from django.conf.urls import url, include

from home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    #设置默认首页
    url('^$',views.index,name='index'),
    url('home/', include('apps.home.urls')),
    url('account/', include('apps.accoount.urls')),
    url('cart/', include('apps.cart.urls')),
    url('cate_detail', include('apps.cate_detail.urls')),
    url('order', include('apps.order.urls')),
    url('pay', include('apps.pay.urls')),
    url('shop_detail', include('apps.shop_detail.urls')),

]
