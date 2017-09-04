from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^comment/(?P<pk>\d+)/delete$', views.DeleteComment, name='comment.delete'),
    url(r'^amp/(?P<slug>[-\w\d]+)$', views.Amp, name='show'),
    url(r'^(?P<slug>[-\w\d]+)$', views.Show, name='show'),
    url(r'^(?P<slug>[-\w\d]+)/edit$', views.Edit, name='edit'),
    url(r'^(?P<slug>[-\w\d]+)/delete$', views.Delete, name='delete'),
    url(r'^(?P<slug>[-\w\d]+)/comment$', views.PostComment, name='comment'),
    url(r'^label/(?P<name>\w+)$', views.Label, name='labels'),
]
