from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'categories/(?P<category_id>\d+)/hotskus/$', views.HotSKUListView.as_view()),
    url(r'categories/(?P<category_id>\d+)/skus/$', views.HotSKUListView.as_view()),
]
