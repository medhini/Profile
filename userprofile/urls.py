from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^profile/$', 'userprofile.views.user_profile'),
	 url(r'^profile/password_reset_form/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^profile/password_reset_done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^profile/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^profile/password_done/$', 
        'django.contrib.auth.views.password_reset_complete'),
)
