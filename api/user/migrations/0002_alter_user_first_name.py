# Generated by Django 4.2.2 on 2023-06-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=255),
        ),
    ]