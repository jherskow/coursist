# Generated by Django 3.0.7 on 2020-06-27 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("academic_helper", "0008_auto_20200604_0112"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="ratingdummy", unique_together={("content_type", "object_id", "name")},),
    ]
