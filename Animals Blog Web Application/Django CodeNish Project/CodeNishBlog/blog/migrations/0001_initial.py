# Generated by Django 5.0.2 on 2024-02-23 06:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogTable',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
