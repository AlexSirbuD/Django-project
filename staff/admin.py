from django.contrib import admin


from .models import *


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_id', 'slug', 'title', 'price', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title', 'price')
    search_fields = ('title', 'content', 'price')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    



admin.site.register(Staff, StaffAdmin)
