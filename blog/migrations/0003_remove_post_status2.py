# Generated by Django 4.1 on 2022-08-25 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_status2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status2',
        ),
    ]
