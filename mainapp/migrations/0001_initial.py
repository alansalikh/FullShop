# Generated by Django 4.1.5 on 2023-01-18 14:06

import autoslug.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='??????')),
                ('last_name', models.CharField(max_length=255, verbose_name='??????????????')),
                ('phone', models.CharField(max_length=12, verbose_name='??????????????')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='????????')),
                ('status', models.CharField(choices=[('new', '?????????? ??????????'), ('in_progress', '?????????? ?? ??????????????????'), ('ready', '?????????? ??????????'), ('completed', '?????????? ????????????????')], default='new', max_length=100, verbose_name='???????????? ????????????')),
                ('buying_type', models.CharField(choices=[('self', '??????????????????'), ('delivery', '????????????????')], default='self', max_length=100, verbose_name='?????? ????????????')),
                ('comment', models.TextField(verbose_name='?????????????????????? ?? ????????????')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='???????? ???????????????? ????????????')),
                ('order_date', models.DateTimeField(default=datetime.datetime(2023, 1, 18, 14, 6, 13, 962797, tzinfo=datetime.timezone.utc), verbose_name='???????? ?????????????????? ????????????')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]
