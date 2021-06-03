# Generated by Django 3.2 on 2021-06-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.TextField(blank=True, choices=[('LG', 'Large'), ('MD', 'Medium'), ('SM', 'Small')], default='Medium', max_length=100, null=True),
        ),
    ]