# Generated by Django 4.1.3 on 2023-01-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='ProfilePicture'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='file',
            field=models.FileField(upload_to='VerificationFiless'),
        ),
    ]
