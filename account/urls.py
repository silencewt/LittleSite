from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^register$', 'account.views.register'),
    url(r'^login$', 'account.views.login'),
    url(r'^logout$', 'account.views.logout'),
    url(r'^self$', 'account.views.showself'),
    url(r'^(?P<id>\d*)$', 'account.views.showaccount'),
)