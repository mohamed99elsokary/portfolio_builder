# Generated by Django 3.2.6 on 2021-08-21 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profiles_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='FocusPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=150)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profiles')),
            ],
        ),
    ]
