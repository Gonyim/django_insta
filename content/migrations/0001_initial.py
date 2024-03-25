# Generated by Django 5.0.3 on 2024-03-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('profile_pic', models.TextField()),
                ('user_id', models.TextField()),
                ('like_count', models.IntegerField()),
            ],
        ),
    ]