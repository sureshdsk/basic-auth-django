from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.page_index, name='page_index'),
    url(r'^(?P<slug>[a-z0-9-]+)/$', views.page_view, name='page_view'),
]