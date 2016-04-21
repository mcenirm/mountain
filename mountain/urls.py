from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .views import ApiEndpoint

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^api/hello', ApiEndpoint.as_view()),
]
