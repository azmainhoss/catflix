# Generated by Django 4.1.7 on 2023-02-16 16:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('watch_count', models.IntegerField(default=0)),
                ('file', models.FileField(upload_to='movies/')),
                ('preview_image', models.ImageField(upload_to='preview_images/')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catflix_app.category')),
                ('tags', models.ManyToManyField(to='catflix_app.tag')),
            ],
        ),
    ]
