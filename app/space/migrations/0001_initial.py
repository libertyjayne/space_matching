# Generated by Django 2.1.15 on 2021-10-09 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import space.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('max_people', models.IntegerField()),
                ('min_people', models.IntegerField()),
                ('max_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('days_per_week', models.IntegerField()),
                ('link', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=space.models.space_image_file_path)),
                ('has_place', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
