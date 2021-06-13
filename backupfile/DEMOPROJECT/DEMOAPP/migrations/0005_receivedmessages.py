# Generated by Django 3.1.6 on 2021-06-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP', '0004_messages_sent_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedMessages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(max_length=15)),
                ('body', models.CharField(max_length=200)),
                ('received_date', models.DateField()),
            ],
        ),
    ]