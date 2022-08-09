# Generated by Django 3.2 on 2022-07-19 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_id'),
        ('shop', '0002_auto_20220719_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
    ]
