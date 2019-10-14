from celery import Celery

# 创建celery应用
celery_app = Celery('meiduo_project')

# 导入celery配置
celery_app.config_from_object('celery_tasks.config')

# 自动注册celery任务
celery_app.autodiscover_tasks(['celery_tasks.sms'])
