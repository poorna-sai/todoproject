# Generated by Django 5.0.6 on 2024-06-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_task_image_alter_task_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='no image', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='video',
            field=models.FileField(default='no video', upload_to='media/'),
        ),
    ]
