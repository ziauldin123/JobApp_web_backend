# Generated by Django 3.0.7 on 2020-06-23 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0003_job_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='type',
            new_name='jtype',
        ),
    ]
