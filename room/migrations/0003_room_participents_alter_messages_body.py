# Generated by Django 4.0.6 on 2022-09-20 05:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0002_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participents',
            field=models.ManyToManyField(blank=True, related_name='participents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]