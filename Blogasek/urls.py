from django.conf.urls import patterns, include, url
#from rest_framework import routers
from Blog import views

from django.contrib import admin
admin.autodiscover()

#router = routers.DefaultRouter()
#router.register(r'users', views.UserView)
#router.register(r'entries', views.EntryView)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Blogasek.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.login_view, name='login'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^register$', views.register_view, name='logout'),
	url(r'^api-root/', include('Blog.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
