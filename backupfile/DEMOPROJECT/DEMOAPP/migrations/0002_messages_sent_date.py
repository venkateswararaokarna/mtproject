# Generated by Django 3.1.6 on 2021-06-10 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='sent_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]