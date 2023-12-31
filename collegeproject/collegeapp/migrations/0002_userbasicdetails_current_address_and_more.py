# Generated by Django 4.1.7 on 2023-11-05 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collegeapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userbasicdetails",
            name="current_address",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="userbasicdetails",
            name="permanant_address",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="userbasicdetails",
            name="first_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="userbasicdetails",
            name="last_name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
