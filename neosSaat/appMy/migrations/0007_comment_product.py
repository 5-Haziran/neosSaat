# Generated by Django 4.2.1 on 2023-08-31 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0006_remove_comment_comment_remove_product_productsıze_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.product', verbose_name='Ürün'),
        ),
    ]
