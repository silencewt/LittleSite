from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	# url for js, pic & css 

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'testsite.views.welcome'),
    url(r'^account/', include('account.urls')),
    url(r'^share/', include('share.urls')),
    url(r'^google','testsite.views.google'),
)
