# _*_encoding:utf-8_*_
__author__ = 'chmi'
__data__ = '2018/6/24 23:40'

import xadmin
from .models import Course, Lession, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'studenta', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class LessionAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name', 'add_time']
    # 课程名的外键
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lession', 'name', 'add_time']
    search_fields = ['lession', 'name', 'add_time']
    list_filter = ['lession__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['lession', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lession, LessionAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
