# Generated by Django 4.0.4 on 2023-04-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='', max_length=512, verbose_name='제목')),
                ('introduction', models.TextField(blank=True, default='', max_length=1024, verbose_name='소개')),
                ('youtube_link', models.CharField(blank=True, default='', max_length=2048, verbose_name='유튜브 링크')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
                'db_table': 'videos',
            },
        ),
    ]
