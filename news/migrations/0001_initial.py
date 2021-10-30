# Generated by Django 3.2.7 on 2021-10-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(default='news/images/', upload_to='news/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]