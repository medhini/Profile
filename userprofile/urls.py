from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^profile/$', 'userprofile.views.user_profile'),
    	url(r'^accounts/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/accounts/password/reset/done/'},
        name="password_reset"),
    (r'^accounts/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password/done/'}),
    (r'^accounts/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
)

