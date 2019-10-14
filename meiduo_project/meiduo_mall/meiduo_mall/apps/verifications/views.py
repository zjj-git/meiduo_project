import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from verifications import constants, serializers
from meiduo_mall.libs.captcha.captcha import captcha
from celery_tasks.sms.tasks import send_sms_code


class ImageCodeView(APIView):
    """
    图片验证码
    """

    def get(self, request, image_code_id):
        """
        获取图片验证码
        """
        # 生成验证码图片
        name, text, image = captcha.generate_captcha()

        # 连接redis数据库
        redis_conn = get_redis_connection("verify_codes")
        redis_conn.setex("img_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)

        # 指定返回的数据类型
        return HttpResponse(image, content_type="images/jpg")


class SMSCodeView(GenericAPIView):
    """
    短信验证码
    """
    serializer_class = serializers.CheckImageCodeSerialzier

    def get(self, request, mobile):
        """
        创建短信验证码
        """
        # 判断图片验证码, 判断是否在60s内
        serializer = self.get_serializer(data=request.query_params)
        # 校验
        serializer.is_valid(raise_exception=True)

        # 生成短信验证码
        sms_code = "%06d" % random.randint(0, 999999)
        print("短信验证码内容是：%s" % sms_code)

        # 保存短信验证码与发送记录
        redis_conn = get_redis_connection('verify_codes')
        pl = redis_conn.pipeline()
        # 短讯验证码有效期
        pl.setex("sms_%s" % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 短讯验证码发送间隔
        pl.setex("send_flag_%s" % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
        pl.execute()

        # 发送短信验证码
        send_sms_code.delay(mobile, sms_code)
        # print(send_sms_code)
        # print(send_sms_code(mobile,sms_code))
        return Response({"message": "OK"}, status.HTTP_200_OK)
