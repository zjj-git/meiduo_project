#!/bin/bash

# 执行静态服务器
cd /home/zjj/PycharmProjects/django_project/meiduo_project/front_end
# &符号表示让改命令后台运行
live-server &

# 执行异步任务
cd /home/zjj/PycharmProjects/django_project/meiduo_project/meiduo_mall
celery -A celery_tasks.main worker -l info
