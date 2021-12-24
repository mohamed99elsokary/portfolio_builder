# Generated by Django 3.2.6 on 2021-08-19 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.categories')),
            ],
        ),
        migrations.CreateModel(
            name='user_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projects_number', models.IntegerField(blank=True, null=True)),
                ('sample_url', models.URLField(blank=True, null=True)),
                ('category_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='skills.categories')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_skills', to='profiles.profiles')),
                ('skills_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skills')),
            ],
        ),
    ]