from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^profile/$', 'userprofile.views.user_profile'),
    	url(r'^profile/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/profile/password/reset/done/'},
        name="password_reset"),
    (r'^profile/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^profile/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/profile/password/done/'}),
    (r'^profile/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
)

