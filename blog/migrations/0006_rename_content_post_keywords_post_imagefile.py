# Generated by Django 4.1 on 2022-08-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='keywords',
        ),
        migrations.AddField(
            model_name='post',
            name='imagefile',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
