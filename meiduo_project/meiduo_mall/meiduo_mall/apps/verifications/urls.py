from django.conf.urls import url

from verifications import views

urlpatterns = [
    url(r'image_codes/(?P<image_code_id>.+)/$', views.ImageCodeView.as_view()),
    url(r'sms_codes/(?P<mobile>.+)/$', views.SMSCodeView.as_view()),
    url(r'sms_codes/$', views.SMSCodeByTokenView.as_view())
]
