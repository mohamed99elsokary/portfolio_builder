# Generated by Django 3.2.5 on 2021-07-25 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profiles_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='languages',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
