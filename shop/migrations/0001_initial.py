# Generated by Django 2.2.6 on 2020-03-16 05:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_number', models.IntegerField(blank=True, null=True)),
                ('ratee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ratee', to=settings.AUTH_USER_MODEL)),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_is_visible', models.BooleanField(default=False)),
                ('school', models.CharField(blank=True, choices=[('SOSE', 'SOSE'), ('SOM', 'SOM'), ('SOSS', 'SOSS'), ('SOH', 'SOH')], default=None, max_length=4, null=True)),
                ('school_is_visible', models.BooleanField(default=False)),
                ('grad_year', models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1859), django.core.validators.MaxValueValidator(9999)])),
                ('gradyr_is_visible', models.BooleanField(default=False)),
                ('major', models.CharField(blank=True, default=None, help_text='Please use the following format: BS CS', max_length=10, null=True)),
                ('major_is_visible', models.BooleanField(default=False)),
                ('trade_pts', models.IntegerField(default=0)),
                ('contact_num', models.CharField(default='', help_text='Please use the following format: +639123456789', max_length=15)),
                ('fb_link', models.CharField(default='facebook.com', help_text='Please use the following format: facebook.com/your.profile', max_length=40)),
                ('display_pic', models.ImageField(default='default-user.jpg', upload_to=shop.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('description', models.TextField(default='')),
                ('category', models.CharField(choices=[('Academic Books', 'Academic Books'), ('Non-Academic Books', 'Non-Academic Books'), ('School Supplies', 'School Supplies'), ('Clothes', 'Clothes'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Events', 'Events'), ('Food', 'Food'), ('Service', 'Service'), ('Cosmetics', 'Cosmetics'), ('Toiletries', 'Toiletries')], default='', max_length=100)),
                ('location', models.CharField(default='Ateneo de Manila University', max_length=200)),
                ('is_sold', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.Item')),
            ],
        ),
    ]
