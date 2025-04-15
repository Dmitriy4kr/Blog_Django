# Generated by Django 5.2 on 2025-04-12 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post_title', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_text', models.TextField()),
                ('title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post_title.posttitle')),
            ],
        ),
    ]
