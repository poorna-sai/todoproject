# Generated by Django 5.0.6 on 2024-06-19 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='No title', max_length=50)),
                ('Description', models.TextField()),
                ('Date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
