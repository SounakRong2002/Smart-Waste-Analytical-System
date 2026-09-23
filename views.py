from django.db.models import Avg, Count
from django.shortcuts import render

from .models import DatasetRecord


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def analytics(request):
    records = DatasetRecord.objects.all()
    summary = records.aggregate(
        total_records=Count("id"),
        countries=Count("country", distinct=True),
        average_measurement=Avg("combined_figures_kg_per_capita_year"),
    )
    summary["average_measurement"] = (
        f"{summary['average_measurement']:.2f}"
        if summary["average_measurement"] is not None
        else None
    )
    summary["data_variables"] = 7
    return render(request, "analytics.html", {"summary": summary})


def members(request):
    return render(request, "members.html")


def contact(request):
    return render(request, "contact.html")