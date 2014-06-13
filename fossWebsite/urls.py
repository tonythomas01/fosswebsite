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
    url(r'^information/(?P<info_type>\w+)','info_det'),
    url(r'^information/','info_page'),

)
urlpatterns += patterns('register.views',
    url(r'^register/login$', 'login'),
    url(r'^register/logout$','logout'),
    url(r'^register/new','newregister'),
    url(r'^register/(?P<user_name>\w+)/mypage','mypage'),
    url(r'^register/(?P<user_name>\w+)/profile','profile'),
    url(r'^register/(?P<user_name>\w+)/change_password','change_password'),
)

urlpatterns += patterns('achievement.views',
    url(r'^achievement/viewall$','achieve_viewall'),
    url(r'^contribution/viewall$', 'contrib_viewall'),
    url(r'^article/viewall$', 'article_viewall'),
    url(r'^gsoc/viewall$', 'gsoc_viewall'),
    url(r'^speaker/viewall$', 'speaker_viewall'),

)
