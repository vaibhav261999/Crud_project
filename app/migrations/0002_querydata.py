# Generated by Django 5.0.1 on 2024-01-12 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Query', models.CharField(max_length=200)),
                ('QueryEmail', models.CharField(max_length=200)),
            ],
        ),
    ]
