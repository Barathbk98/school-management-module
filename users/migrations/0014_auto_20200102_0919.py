# Generated by Django 3.0.1 on 2020-01-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200102_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='students_profile_pics'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='teachers_profile_pics'),
        ),
    ]
