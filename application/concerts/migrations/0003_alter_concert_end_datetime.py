# Generated by Django 5.1.6 on 2025-02-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("concerts", "0002_concert_poster"),
    ]

    operations = [
        migrations.AlterField(
            model_name="concert",
            name="end_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Время начала"
            ),
        ),
    ]
