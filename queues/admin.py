from django.contrib import admin

from . import models


class QueueAdmin(admin.ModelAdmin):
    list_display = ('queue_number', 'status', 'queue_type')


admin.site.register(models.Queue, QueueAdmin)
