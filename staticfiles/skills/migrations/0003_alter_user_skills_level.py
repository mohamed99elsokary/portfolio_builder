# Generated by Django 3.2.6 on 2021-08-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_user_skills_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_skills',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
