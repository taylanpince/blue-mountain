from django.contrib import admin

from contests.actions import export_csv
from contests.models import Contest, ContestEntry, ContestWinner


class ContestAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "flight_date")
    search_fields = ("title",)

    save_on_top = True
    save_as = True


class ContestEntryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "contest", "email", "entry_date", "newsletter", "source")
    list_filter = ("contest", "newsletter", "source")
    actions = [export_csv]

    save_on_top = True


class ContestWinnerAdmin(admin.ModelAdmin):
    list_display = ("name", "contest")
    list_filter = ("contest",)

    save_on_top = True


admin.site.register(Contest, ContestAdmin)
admin.site.register(ContestEntry, ContestEntryAdmin)
admin.site.register(ContestWinner, ContestWinnerAdmin)
