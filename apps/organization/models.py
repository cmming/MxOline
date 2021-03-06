# _*_encoding:utf-8_*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市名称')
    desc = models.CharField(max_length=300, verbose_name='描述')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='课程封面')
    click_nums = models.IntegerField(default=0, verbose_name='电击次数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    address = models.CharField(max_length=150, verbose_name='机构地址')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
    city = models.ForeignKey(CityDict)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(max_length=20, verbose_name='教师名称')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='工作公司')
    work_position = models.CharField(max_length=50, verbose_name='职位')
    point = models.CharField(max_length=50, verbose_name='特点')
    click_nums = models.IntegerField(default=0, verbose_name='电击次数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
