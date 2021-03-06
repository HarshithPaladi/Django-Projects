# Generated by Django 4.0.2 on 2022-02-12 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('register_no', models.IntegerField()),
                ('mark_1', models.IntegerField()),
                ('grade_1', models.CharField(max_length=1)),
                ('mark_2', models.IntegerField()),
                ('grade_2', models.CharField(max_length=1)),
                ('mark_3', models.IntegerField()),
                ('grade_3', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
