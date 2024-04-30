# Generated by Django 5.0.4 on 2024-04-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('roll', models.AutoField(primary_key=True, serialize=False)),
                ('registrant_id', models.BigIntegerField()),
                ('Married', models.BooleanField()),
                ('min_salary', models.SmallIntegerField()),
                ('max_salary', models.BigIntegerField()),
                ('About_you', models.TextField()),
            ],
        ),
    ]