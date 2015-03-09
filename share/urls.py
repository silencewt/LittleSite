from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'share.views.show'),
    url(r'^submit$', 'share.views.create'),
    url(r'^text/(?P<id>\d*)$', 'share.views.showtext'),
    url(r'^new$','share.views.create'),
)