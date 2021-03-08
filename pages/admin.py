from django.contrib import admin

from pages.models import Expert, Meeting

class MeetingAdmin(admin.ModelAdmin):
    list_display = ("user", "objective")

admin.site.register(Expert)
admin.site.register(Meeting, MeetingAdmin)