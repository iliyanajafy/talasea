# Generated by Django 5.1.1 on 2024-10-13 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_review',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='blog.blog'),
        ),
    ]