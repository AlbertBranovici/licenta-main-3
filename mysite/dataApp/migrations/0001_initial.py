# Generated by Django 5.0.4 on 2024-04-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tableLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=150)),
            ],
        ),
    ]