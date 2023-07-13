# Generated by Django 3.2.10 on 2023-07-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230713_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(max_length=50, null=True, verbose_name='태그'),
        ),
        migrations.AlterField(
            model_name='post',
            name='region',
            field=models.CharField(max_length=20, null=True, verbose_name='구'),
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
