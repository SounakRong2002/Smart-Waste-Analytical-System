# Food waste dataset

`food_waste.csv` contains the imported country-level source dataset. It must contain one row per country and these columns:

- `country`
- `region`
- `combined_figures_kg_per_capita_year`
- `household_estimate_kg_per_capita_year`
- `household_estimate_tonnes_year`
- `retail_estimate_kg_per_capita_year`
- `retail_estimate_tonnes_year`
- `food_service_estimate_kg_per_capita_year`
- `food_service_estimate_tonnes_year`
- `confidence`
- `m49_code`

Blank numeric cells are stored as missing values. Import the data with:

```text
python manage.py migrate
python manage.py import_food_waste data/food_waste.csv --replace
```

The importer also accepts the original descriptive headers from `cleaned_food_waste_data.csv` and maps them into the database fields above.
