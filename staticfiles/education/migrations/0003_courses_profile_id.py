# Generated by Django 3.2.6 on 2021-08-19 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_languages_level'),
        ('education', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='profile_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_courses', to='profiles.profiles'),
        ),
    ]
