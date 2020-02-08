# Generated by Django 2.0.1 on 2019-12-31 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191230_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='students',
            name='standard',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Classes'),
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='standard',
        ),
        migrations.AddField(
            model_name='teachers',
            name='standard',
            field=models.ManyToManyField(to='users.Classes'),
        ),
    ]
