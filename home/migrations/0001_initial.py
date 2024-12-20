# Generated by Django 5.1.1 on 2024-12-09 16:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shop',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('itemid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
