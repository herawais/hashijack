from django.conf.urls import url
from hashtaghighjack import views

urlpatterns = [
    url(r'^$', views.hijack, name='hijack'),
]
