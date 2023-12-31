# Generated by Django 3.2.6 on 2021-08-29 19:36

import autoslug.fields
import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('customers', '0001_initial'),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.CharField(blank=True, choices=[('m', 'M'), ('l', 'L'), ('xl', 'XL')], max_length=10, null=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('available', models.BooleanField(default=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('numbersOfReview', models.IntegerField(blank=True, default=0, null=True)),
                ('countInStock', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('wishlist', models.ManyToManyField(to='customers.Customer')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
