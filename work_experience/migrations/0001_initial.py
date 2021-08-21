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
            name='organizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='upload/organizations_icon/')),
                ('icon_url', models.URLField(blank=True, default=None, null=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('organizations_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_experience.organizations')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_work_experience', to='profiles.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=150, null=True)),
                ('organization_id', models.ManyToManyField(related_name='organization_tags', to='work_experience.organizations')),
            ],
        ),
        migrations.CreateModel(
            name='bullet_points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_text', models.TextField(blank=True, max_length=100, null=True)),
                ('work_experience_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_bullet_points', to='work_experience.work_experience')),
            ],
        ),
    ]
