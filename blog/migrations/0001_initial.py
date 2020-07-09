# Generated by Django 3.0.8 on 2020-07-09 08:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('bio', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_posted', models.DateField(default=datetime.date.today, help_text='Date when the post was uploaded')),
                ('description', models.TextField(help_text='Enter the content for the blog post', max_length=4000)),
                ('blogger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Blogger')),
            ],
        ),
    ]
