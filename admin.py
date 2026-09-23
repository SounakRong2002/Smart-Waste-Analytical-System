from django.contrib import admin

from .models import DatasetRecord


@admin.register(DatasetRecord)
class DatasetRecordAdmin(admin.ModelAdmin):
	list_display = ("country", "region", "combined_figures_kg_per_capita_year", "imported_at")
	search_fields = ("country", "region")
	list_filter = ("region",)
