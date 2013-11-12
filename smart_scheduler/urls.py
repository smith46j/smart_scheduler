from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from schedule.views import CalendarTemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'smart_scheduler.views.home', name='home'),
    # url(r'^smart_scheduler/', include('smart_scheduler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Calendar/', CalendarTemplateView.as_view(), name='Calendar_template_view') 
)
