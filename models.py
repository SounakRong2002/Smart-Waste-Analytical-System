from django.db import models


class DatasetRecord(models.Model):
	country = models.CharField(max_length=120, unique=True)
	region = models.CharField(max_length=120, blank=True)
	confidence = models.CharField(max_length=40, blank=True)
	m49_code = models.PositiveIntegerField(null=True, blank=True)
	combined_figures_kg_per_capita_year = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	household_estimate_kg_per_capita_year = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	household_estimate_tonnes_year = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
	retail_estimate_kg_per_capita_year = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	retail_estimate_tonnes_year = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
	food_service_estimate_kg_per_capita_year = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	food_service_estimate_tonnes_year = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
	imported_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["country"]

	def __str__(self):
		return self.country
