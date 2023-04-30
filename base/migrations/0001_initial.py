# Generated by Django 4.1.7 on 2023-04-25 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.IntegerField(blank=True, null=True)),
                ('current_read_books', models.IntegerField(blank=True, null=True)),
                ('books_read', models.CharField(blank=True, max_length=4000000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChallengeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('b_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('author', models.CharField(blank=True, max_length=1000, null=True)),
                ('isbn', models.CharField(blank=True, max_length=1000, null=True)),
                ('published_year', models.CharField(blank=True, max_length=1000, null=True)),
                ('num_pages', models.IntegerField(blank=True, default=200, null=True)),
                ('language', models.CharField(blank=True, choices=[('AR', 'Arabic'), ('EN', 'English'), ('FR', 'French')], default='EN', max_length=2, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('defaultImage', models.CharField(blank=True, max_length=1000, null=True)),
                ('publisher', models.CharField(blank=True, max_length=1000, null=True)),
                ('category', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('available', models.BooleanField(blank=True, default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, default='/store_placeholder.png', null=True, upload_to='')),
                ('wilaya', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('isbn', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.store'),
        ),
        migrations.CreateModel(
            name='ChallengeProgres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.PositiveIntegerField(default=0)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenge_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.challengetype'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]