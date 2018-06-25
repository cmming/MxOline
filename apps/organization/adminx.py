# _*_encoding:utf-8_*_
__author__ = 'chmi'
__data__ = '2018/6/24 23:40'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class ECityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


xadmin.site.register(CityDict, ECityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'image', 'click_nums', 'fav_nums', 'address', 'add_time', 'city']
    search_fields = ['name', 'desc', 'image', 'click_nums', 'fav_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'image', 'click_nums', 'fav_nums', 'address', 'add_time', 'city']


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'point', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'point', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'point', 'click_nums', 'fav_nums',
                   'add_time']


xadmin.site.register(Teacher, TeacherAdmin)
