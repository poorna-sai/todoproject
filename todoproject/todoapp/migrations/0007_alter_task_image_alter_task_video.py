# Generated by Django 5.0.6 on 2024-06-22 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_task_image_alter_task_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='no image', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='task',
            name='video',
            field=models.FileField(default='no video', upload_to='videos/'),
        ),
    ]