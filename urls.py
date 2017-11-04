from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csvt07.views.home', name='home'),
    # url(r'^csvt07/', include('csvt07.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/show_author/$','blog.views.show_author'),
    url(r'^blog/show_book/$','blog.views.show_book'),
    url(r'^blog/register/$','blog.views.register'),

)
