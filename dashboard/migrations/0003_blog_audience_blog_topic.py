# Generated by Django 4.2.13 on 2024-07-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_blog_alter_profile_uniqueid_blogsection_blog_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='audience',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='topic',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
