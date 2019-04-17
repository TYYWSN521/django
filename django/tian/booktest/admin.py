from django.contrib import admin
from .models import BookInfo, HeroInfo
# Register your models here.


class HeroInfoline(admin.StackedInline):
    model = HeroInfo
    extra = 1


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'sex', 'skill']
    list_fifter= ['name']
    search_fields = ['sex']


admin.site.register(BookInfo)
admin.site.register(HeroInfo, HeroInfoAdmin)
