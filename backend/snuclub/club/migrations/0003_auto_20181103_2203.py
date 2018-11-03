# Generated by Django 2.1.2 on 2018-11-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20181103_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='staffs', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='club',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='clubs', to='club.Tag'),
        ),
    ]
