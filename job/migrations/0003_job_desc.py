# Generated by Django 4.0.6 on 2022-07-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='desc',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
