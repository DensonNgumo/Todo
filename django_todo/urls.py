from django.conf.urls import url, include
from django.contrib import admin
from todos import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'), 
    url(r'^details/(?P<todo_id>[0-9]+)/$',views.details,name='details'),
    url(r'^add/',views.add,name='add'),
]

