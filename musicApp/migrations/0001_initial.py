# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=200)),
                ('album_logo', models.CharField(max_length=1000)),
                ('album_released', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=200)),
                ('file_type', models.CharField(max_length=20)),
                ('song_url', models.CharField(max_length=500, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicApp.Album')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicApp.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='musicApp.Artist'),
        ),
    ]
