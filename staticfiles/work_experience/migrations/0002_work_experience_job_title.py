# Generated by Django 3.2.9 on 2021-12-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_experience',
            name='job_title',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
