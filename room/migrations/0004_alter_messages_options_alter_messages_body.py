# Generated by Django 4.0.6 on 2022-09-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room_participents_alter_messages_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ['-created', '-updated']},
        ),
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
