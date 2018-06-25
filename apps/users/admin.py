from django.contrib import admin

# Register your models here.

from .models import UserProfile
from .models import EmailVerifyRecord
from .models import Banner


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Banner, BannerAdmin)
