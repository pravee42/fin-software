# Generated by Django 3.2 on 2022-07-21 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumerdetails',
            name='last_collected',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
