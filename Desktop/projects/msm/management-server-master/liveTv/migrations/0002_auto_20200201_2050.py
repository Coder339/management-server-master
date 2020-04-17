# Generated by Django 3.0 on 2020-02-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveTv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='adult',
            new_name='is_adult',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='thumbnail_autogenerated',
        ),
        migrations.RemoveField(
            model_name='channels',
            name='max_recording_time',
        ),
        migrations.RemoveField(
            model_name='channels',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='channels',
            name='EPG_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='channels',
            name='description',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='background_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.RemoveField(
            model_name='channels',
            name='category',
        ),
        migrations.AddField(
            model_name='channels',
            name='category',
            field=models.ManyToManyField(related_name='category', to='liveTv.Categories'),
        ),
        migrations.AlterField(
            model_name='channels',
            name='channel_image',
            field=models.FileField(upload_to=''),
        ),
    ]