# Generated by Django 4.1 on 2022-11-03 23:08

from django.db import migrations

def add_categories(apps, schema_editor):
    fixed_categories = ["Art", "Books", "Computers", "Cars", "Home", "Tavel",
    "Clothes", "Electronics", "Furtniture", "Tools", "Other"]
    Categories = apps.get_model("auctions", "Categories")
    for category in fixed_categories:
        obj = Categories(categories=category)
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_categories)
    ]
