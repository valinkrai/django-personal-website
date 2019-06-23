# Generated by Django 2.2.2 on 2019-06-23 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('last_modified_date_time', models.DateTimeField(auto_now=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('hide', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CurrentlyDoing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('last_modified_date_time', models.DateTimeField(auto_now=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField(null=True)),
                ('done', models.BooleanField()),
                ('hide', models.BooleanField()),
            ],
        ),
    ]
