# Generated by Django 3.1.2 on 2020-10-18 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20201016_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
