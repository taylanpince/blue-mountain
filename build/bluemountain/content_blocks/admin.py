from django.contrib import admin

from content_blocks.models import ContentBlock


class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", "slug")
    save_on_top = True
    prepopulated_fields = {
        "slug": ("title", )
    }

    fieldsets = (
        (None, {
            "fields": (("title", "slug"), "content"),
        }),
    )


admin.site.register(ContentBlock, ContentBlockAdmin)
