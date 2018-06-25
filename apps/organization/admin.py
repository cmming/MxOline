from django.contrib import admin

from .models import CityDict
from .models import CourseOrg
from .models import Teacher


# Register your models here.

class CityDictAdmin(admin.ModelAdmin):
    pass


admin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)
