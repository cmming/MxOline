from django.contrib import admin

from .models import Course
from .models import Lession
from .models import Video
from .models import CourseResource


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)


class LessionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lession, LessionAdmin)


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)


class CourseResourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseResource, CourseResourceAdmin)
