from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import evaluate.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', evaluate.views.index, name='index'),
]
