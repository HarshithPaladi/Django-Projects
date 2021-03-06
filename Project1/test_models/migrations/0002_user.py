# Generated by Django 4.0.2 on 2022-02-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
