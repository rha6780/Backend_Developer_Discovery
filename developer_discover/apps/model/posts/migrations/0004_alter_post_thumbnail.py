# Generated by Django 4.0.4 on 2023-06-14 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='썸네일'),
        ),
    ]