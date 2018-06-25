# _*_encoding:utf-8_*_
__author__ = 'chmi'
__data__ = '2018/6/24 17:40'

import xadmin
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
