# Generated by Django 2.1.2 on 2019-10-18 10:18

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191018_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategory',
            name='desc_detail',
        ),
        migrations.RemoveField(
            model_name='goodscategory',
            name='desc_pack',
        ),
        migrations.RemoveField(
            model_name='goodscategory',
            name='desc_service',
        ),
        migrations.AddField(
            model_name='goods',
            name='desc_detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='详细介绍'),
        ),
        migrations.AddField(
            model_name='goods',
            name='desc_pack',
            field=ckeditor.fields.RichTextField(default='', verbose_name='包装信息'),
        ),
        migrations.AddField(
            model_name='goods',
            name='desc_service',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='售后服务'),
        ),
    ]
