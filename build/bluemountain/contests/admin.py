from django.contrib import admin

from contests.models import Contest, ContestEntry, ContestWinner


class ContestAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date")
    search_fields = ("title",)

    save_on_top = True


class ContestEntryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "contest", "email", "entry_date", "newsletter")
    list_filter = ("contest", "newsletter")

    save_on_top = True


class ContestWinnerAdmin(admin.ModelAdmin):
    list_display = ("name", "contest")
    list_filter = ("contest",)

    save_on_top = True


admin.site.register(Contest, ContestAdmin)
admin.site.register(ContestEntry, ContestEntryAdmin)
admin.site.register(ContestWinner, ContestWinnerAdmin)
