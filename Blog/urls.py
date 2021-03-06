from django.conf.urls import patterns, include, url
from Blog import views

urlpatterns = patterns('',
	url(r'user/$', views.UserView.as_view(), name='user-list'),
	url(r'entries/$', views.EntryView.as_view(), name='entries'),
	url(r'comments/$', views.CommentView.as_view(), name='entries'),
	url(r'commentsedit/(?P<pk>\d+)/$', views.CommentEditView.as_view(), name='entries')
)
