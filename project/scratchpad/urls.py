from django.conf.urls import patterns, include, url
from django.views.generic import DetailView
from scratchpad.models import Note

from endless_pagination.views import AjaxListView

urlpatterns = patterns('',
    url(r'(?P<pk>\d+)/(?P<slug>[-\w]+)', DetailView.as_view(model=Note), name='note-detail'),
    url(r'(?P<pk>\d+)', DetailView.as_view(model=Note), name='note-detail-short'), #todo: have it redirect to correct slug.
    url(r'', AjaxListView.as_view(model=Note), name='note-endless'),
)
