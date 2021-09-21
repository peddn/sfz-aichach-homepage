# Generated by Django 3.2.7 on 2021-09-19 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('content', '0002_rename_blogindexpage_contentpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
