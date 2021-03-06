# Generated by Django 3.0.4 on 2020-03-05 19:44

import Board.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('text_book', models.CharField(max_length=180)),
                ('post_type', models.CharField(choices=[('01', 'buyer'), ('02', 'seller')], default='01', max_length=2)),
                ('price', models.FloatField()),
                ('picture', models.FilePathField(path=Board.models.images_path)),
                ('pose_status', models.CharField(choices=[('01', 'Post Opened'), ('02', 'Post Closed')], default='01', max_length=2)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=255)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.Post')),
            ],
        ),
    ]
