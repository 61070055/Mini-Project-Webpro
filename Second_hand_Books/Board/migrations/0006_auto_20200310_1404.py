# Generated by Django 3.0.4 on 2020-03-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0005_auto_20200310_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pose_status',
            new_name='post_status',
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]