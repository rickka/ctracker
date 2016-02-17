from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from smsremind.views import *
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/','smsremind.views.index', name='index'),
    
    url(r'^add_contract/', 'smsremind.views.add_contract', name='add_contract'),
    url(r'^contractlist/', 'smsremind.views.contractlist', name='contractlist'),
)
