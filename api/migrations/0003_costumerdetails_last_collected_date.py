# Generated by Django 3.2 on 2022-07-21 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_costumerdetails_last_collected'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumerdetails',
            name='last_collected_date',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
