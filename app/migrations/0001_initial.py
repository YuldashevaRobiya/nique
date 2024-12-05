# Generated by Django 5.1.3 on 2024-11-12 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_one', models.CharField(max_length=100)),
                ('title_two', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlogCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='blog_image')),
                ('date', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('paragrph', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title_one', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='blog_post_images')),
                ('text_two', models.CharField(max_length=255)),
                ('description_two', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('i_name', models.CharField(max_length=100)),
                ('i_number', models.CharField(max_length=100)),
                ('i_date', models.IntegerField()),
                ('i_time', models.DateTimeField()),
                ('button', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookTable_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('button', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_1', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_1', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_1', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('title_1', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=100)),
                ('work_time', models.DateTimeField()),
                ('image', models.ImageField(null=True, upload_to='back_img')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_one', models.CharField(max_length=100)),
                ('title_two', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShopCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='card_image')),
                ('button', models.CharField(max_length=100)),
                ('title_one', models.CharField(max_length=100)),
                ('title_two', models.CharField(max_length=100)),
                ('title_three', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=100)),
                ('contact', models.ImageField(null=True, upload_to='icon')),
            ],
        ),
        migrations.CreateModel(
            name='WorkShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_1', models.CharField(max_length=100)),
                ('title_2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkShopDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('teacher', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkShopInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_one', models.CharField(max_length=255)),
                ('title_two', models.CharField(max_length=255)),
                ('title_three', models.CharField(max_length=255)),
                ('title_button', models.CharField(max_length=255)),
                ('title_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='foods')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('discont', models.IntegerField()),
                ('is_food', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.foodcategory')),
            ],
        ),
    ]
