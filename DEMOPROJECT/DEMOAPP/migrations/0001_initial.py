# Generated by Django 3.1.6 on 2021-06-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=200)),
            ],
        ),
    ]
