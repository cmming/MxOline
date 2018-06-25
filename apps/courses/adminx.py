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


xadmin.site.register(Course, CourseAdmin)
