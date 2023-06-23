# Generated by Django 4.2.2 on 2023-06-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyFile",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("file", models.FileField(upload_to="myFile")),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
    ]
