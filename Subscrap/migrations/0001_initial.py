# Generated by Django 3.2.9 on 2021-12-19 01:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prebuildsublist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/prestored')),
                ('website', models.URLField(blank=True, max_length=250)),
                ('subtype', models.CharField(blank=True, choices=[('Music', 'Music'), ('Video', 'Video'), ('News', 'News'), ('Lifestyle', 'Lifestyle'), ('Access', 'Online Access')], max_length=50)),
            ],
            options={
                'db_table': 'prebuildsublist',
            },
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=30)),
                ('lastname', models.CharField(blank=True, max_length=30)),
                ('profilepic', models.ImageField(default='images/defaultuser.png', upload_to='images')),
                ('Bio', models.TextField(blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='sublist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('cost', models.FloatField(default=0)),
                ('renewalcycle', models.IntegerField(choices=[(1, 'Monthly'), (3, 'Trimester'), (12, 'Yearly')], default=1)),
                ('subtype', models.CharField(blank=True, choices=[('Music', 'Music'), ('Video', 'Video'), ('News', 'News'), ('Lifestyle', 'Lifestyle'), ('Online Access', 'Online Access')], max_length=50)),
                ('image', models.ImageField(default='images/logoemblem.png', upload_to='images')),
                ('website', models.URLField(default='http://127.0.0.1:8000/main/', max_length=250)),
                ('startDate', models.DateField(default=datetime.datetime(2021, 12, 19, 1, 18, 1, 108406))),
                ('dueDate', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_autorenewal', models.BooleanField(default=True)),
                ('is_notified', models.BooleanField(default=False)),
                ('Notes', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sublist',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=15)),
                ('total', models.FloatField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
