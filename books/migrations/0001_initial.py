# Generated by Django 4.1.7 on 2023-04-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(blank=True, max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('cover', models.ImageField(blank=True, max_length=1000, null=True, upload_to='')),
                ('image', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.CharField(blank=True, max_length=1000, null=True)),
                ('published_year', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('num_pages', models.CharField(blank=True, max_length=1000, null=True)),
                ('categories', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
