from pathlib import Path
from tempfile import NamedTemporaryFile

from django.core.management import call_command, CommandError
from django.test import TestCase

from .models import DatasetRecord


class DatasetImportTests(TestCase):
	def create_csv(self, contents):
		source = NamedTemporaryFile(mode="w", suffix=".csv", delete=False)
		source.write(contents)
		source.close()
		self.addCleanup(Path(source.name).unlink)
		return source.name

	def test_import_creates_dataset_record(self):
		csv_path = self.create_csv(
			"Country,combined figures (kg/capita/year),"
			"Household estimate (kg/capita/year),Household estimate (tonnes/year),"
			"Retail estimate (kg/capita/year),Retail estimate (tonnes/year),"
			"Food service estimate (kg/capita/year),Food service estimate (tonnes/year),"
			"Confidence in estimate,M49 code,Region\n"
			"Exampleland,126.79,80.00,1000.00,20.00,250.00,26.79,300.00,"
			"High Confidence,999,Example Region\n"
		)

		call_command("import_food_waste", csv_path)

		record = DatasetRecord.objects.get(country="Exampleland")
		self.assertEqual(record.region, "Example Region")
		self.assertEqual(str(record.combined_figures_kg_per_capita_year), "126.79")

	def test_import_rejects_dataset_without_rows(self):
		csv_path = self.create_csv("country,region\n")

		with self.assertRaises(CommandError):
			call_command("import_food_waste", csv_path)


class AnalyticsViewTests(TestCase):
	def test_analytics_page_uses_empty_state_without_imported_data(self):
		response = self.client.get("/analytics/")

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "<strong>--</strong>", count=3, html=True)
		self.assertNotContains(response, "<strong>141</strong>", html=True)
