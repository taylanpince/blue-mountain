from django.contrib import admin

from content_blocks.models import ContentBlock, Photo


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


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("image", "caption")

    save_on_top = True


admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(Photo, PhotoAdmin)
