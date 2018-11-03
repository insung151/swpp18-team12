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
            name='PromotionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('hits', models.IntegerField(default=0)),
                ('join_start', models.DateTimeField(blank=True, null=True)),
                ('join_end', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promotion_posts', to='accounts.UserProfile')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_posts', to='club.Club')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PromotionPostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='promotion_post_comments', to='accounts.UserProfile')),
                ('promotion_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_post_comments', to='promotion_post.PromotionPost')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
