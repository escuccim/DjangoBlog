from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^logout$', views.Logout, name='logout'),
    url(r'^login$', views.Login, name='login'),
    url(r'^register$', views.Register, name='register'),
    url(r'^comment/(?P<pk>\d+)/delete$', views.DeleteComment, name='comment.delete'),
    url(r'^(?P<slug>[-\w\d]+)$', views.Show, name='show'),
    url(r'^(?P<slug>[-\w\d]+)/comment$', views.PostComment, name='comment'),
    url(r'^label/(?P<name>\w+)$', views.Label, name='labels'),
]
