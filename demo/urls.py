from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^robots\.txt$', TemplateView.as_view(
                template_name='demo/robots.txt', content_type='text/plain')),

    # We override the standard Ditto home page with a slightly different one:
    url(r'^$', view=views.HomeView.as_view(), name='home'),

    url(r'^flickr/', include('ditto.flickr.urls', namespace='flickr')),
    url(r'^pinboard/', include('ditto.pinboard.urls', namespace='pinboard')),
    url(r'^twitter/', include('ditto.twitter.urls', namespace='twitter')),

    # Include the overall, aggregated views:
    url(r'', include('ditto.core.urls', namespace='ditto')),
]

