# Generated by Django 2.1.2 on 2018-11-03 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0002_auto_20181103_2158'),
        ('accounts', '0002_userprofile_favorite_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('overall', models.IntegerField()),
                ('operation', models.IntegerField()),
                ('facility', models.IntegerField()),
                ('newcomer', models.IntegerField()),
                ('compulsory', models.IntegerField()),
                ('meetfreq', models.IntegerField()),
                ('age', models.IntegerField()),
                ('friendliness', models.IntegerField()),
                ('alcohol', models.IntegerField()),
                ('comments', models.TextField(blank=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratings', to='club.Club')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ratings', to='accounts.UserProfile')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
