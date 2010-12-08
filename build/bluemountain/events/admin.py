from django.contrib import admin

from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "order")
    search_fields = ("title", "description", "content")

    save_on_top = True


admin.site.register(Event, EventAdmin)
