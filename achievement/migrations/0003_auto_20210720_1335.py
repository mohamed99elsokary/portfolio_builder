# Generated by Django 3.2.5 on 2021-07-20 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('achievement', '0002_achievement_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='hyperlinks',
            name='award_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='award_hyperlinks', to='achievement.achievement'),
        ),
        migrations.AlterField(
            model_name='hyperlinks',
            name='achievement_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='achievement_hyperlinks', to='achievement.achievement'),
        ),
        migrations.CreateModel(
            name='award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=300, null=True)),
                ('order', models.IntegerField(default=None)),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_awards', to='profiles.profiles')),
            ],
        ),
    ]
