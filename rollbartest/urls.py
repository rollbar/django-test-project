from django.conf.urls import patterns, include, url

from django.contrib import admin

from rollbartest import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rollbartest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^error/', views.error, name='error'),
    url(r'^error2/', views.error, name='error2'),
    url(r'^error3/', views.error, name='rollbartest.error3'),
    url(r'^error4/', views.error, name='rollbartest.fourth.error'),
)
