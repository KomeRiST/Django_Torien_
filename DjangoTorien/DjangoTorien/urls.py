"""
Definition of urls for DjangoTorien.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views
import app.api

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact/$', app.views.contact, name='contact'),
    url(r'^about/$', app.views.about, name='about'),
    url(r'^catalog/$', app.views.catalog, name='catalog'),
    url(r'^collection/(?P<_id>[0-9])/$', app.views.collection, name='collection'),
    url(r'^collections/$', app.views.collections, name='collections'),
    url(r'^collections2/$', app.views.collections2, name='collections2'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'), # login
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'), # logout

    # API url
    url(r'^api/getCategory$', app.api.APIgetcategory, name='APIgetcategory'),
    url(r'^api/getThings', app.api.APIgetthings, name='APIgetthings'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
