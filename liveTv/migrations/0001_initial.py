# Generated by Django 3.0 on 2020-01-23 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('background_image', models.URLField(max_length=255)),
                ('thumbnail_autogenerated', models.URLField(max_length=255)),
                ('adult', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('channel_url', models.URLField(max_length=255)),
                ('channel_image', models.URLField(max_length=255)),
                ('thumbnail', models.URLField(max_length=255)),
                ('max_recording_time', models.IntegerField()),
                ('is_popular', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='liveTv.Categories')),
            ],
            options={
                'verbose_name_plural': 'Channels',
            },
        ),
    ]