from django.contrib import admin
from Home.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt',)
    list_filter = ('alt',)
