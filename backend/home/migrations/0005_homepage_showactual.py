# Generated by Django 3.1.7 on 2021-05-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homepage_actual'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='showActual',
            field=models.BooleanField(default=True),
        ),
    ]
