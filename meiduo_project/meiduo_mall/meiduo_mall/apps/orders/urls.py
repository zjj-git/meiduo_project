from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from orders import views

urlpatterns = [
    url(r'orders/settlement/$', views.OrderSettlementView.as_view()),
    url(r'orders/$', views.SaveOrderView.as_view())
]

rotuer = DefaultRouter()
rotuer.register('orders/info', views.OrdersViewSet, base_name='orders')
urlpatterns += rotuer.urls
