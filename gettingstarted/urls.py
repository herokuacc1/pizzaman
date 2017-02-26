from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^products', hello.views.products, name='products'),
    url(r'^thank', hello.views.thank, name='thank'),
    url(r'^checkout/(?P<id>\d+)/$', hello.views.checkout, name='checkout'),
    url(r'^admin/', include(admin.site.urls)),
]
