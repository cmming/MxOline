from django.contrib import admin

from .models import UserAsk
from .models import CourseComment
from .models import UserFavorite
from .models import UserMessage
from .models import UserCourse


# Register your models here.

class UserAskAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserAsk, UserAskAdmin)


class CourseCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseComment, CourseCommentAdmin)


class UserFavoriteAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserFavorite, UserFavoriteAdmin)


class UserMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserMessage, UserMessageAdmin)


class UserCourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserCourse, UserCourseAdmin)
