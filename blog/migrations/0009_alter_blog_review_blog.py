# Generated by Django 5.1.1 on 2024-12-09 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_review',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
    ]