from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fossWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('fossWebsite.views',
    url(r'^home/$', 'home'),
    url(r'^$','homeredirect'),
    url(r'^search/','search'),
)
urlpatterns += patterns('register.views',
    url(r'^register/login$', 'login'),
    url(r'^register/logout$','logout'),
    url(r'^register/new','newregister'),
    url(r'^register/(?P<user_name>\w+)/mypages','mypages'),
    url(r'^register/(?P<user_name>\w+)/profile','profile'),
    url(r'^register/(?P<user_name>\w+)/change_password','change_password'),
)
