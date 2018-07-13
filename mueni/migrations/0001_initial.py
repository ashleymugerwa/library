# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-10 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('number_of_books', models.CharField(max_length=100)),
                ('awards', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('edition', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('isbn', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mueni.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='LibraryRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned', models.BooleanField(default=False)),
                ('expected_return_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mueni.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('admission_number', models.CharField(max_length=5000)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mueni.State'),
        ),
        migrations.AddField(
            model_name='libraryrecord',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mueni.Member'),
        ),
        migrations.AddField(
            model_name='libraryrecord',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mueni.State'),
        ),
        migrations.AddField(
            model_name='category',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mueni.State'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mueni.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='state',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='mueni.State'),
        ),
    ]
