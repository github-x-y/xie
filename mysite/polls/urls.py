from django.conf.urls import url
from . import  views
urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^sumbit/$',views.detail,name='detail,phone,info'),
        url(r'^sumbit/profile/$',views.profile,name='profile'),
]
