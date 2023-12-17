# Generated by Django 4.2 on 2023-04-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='product_images')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('delete_flag', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'products_master_table',
            },
        ),
    ]