# Generated by Django 5.2 on 2025-06-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0009_delete_sessionrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=100, unique=True)),
                ('file_content', models.TextField()),
            ],
        ),
    ]
