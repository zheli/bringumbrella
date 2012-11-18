from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'bu_django.views.home', name='home'),
	url(r'^form/$', 'signup.views.form', name='form'),
	url(r'^mail_content/', 'bu_django.views.mail_content', name='mail-content'),
	url(r'^accounts/', include('registration.backends.default.urls')),
    # Examples:
    # url(r'^$', 'bu_django.views.home', name='home'),
    # url(r'^bu_django/', include('bu_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)