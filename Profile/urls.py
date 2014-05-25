from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Profile.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),
    url(r'^/$', 'Profile.views.login'),
    url(r'^accounts/login/$', 'Profile.views.login'),
    url(r'^accounts/auth/$', 'Profile.views.auth_view'),
    url(r'^accounts/logout/$', 'Profile.views.logout'),
    url(r'^accounts/loggedin/$', 'Profile.views.loggedin'),
    url(r'^accounts/invalid/$', 'Profile.views.invalid_login'),
    url(r'^accounts/register/$', 'Profile.views.register_user'),
    url(r'^accounts/register_success/$', 'Profile.views.register_success'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userprofile.urls')),
)
