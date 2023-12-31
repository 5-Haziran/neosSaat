# Generated by Django 4.2.1 on 2023-08-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_remove_product_comment_comment_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_img',
            new_name='productİmg',
        ),
        migrations.RenameField(
            model_name='profil',
            old_name='user_img',
            new_name='userİmg',
        ),
        migrations.AlterField(
            model_name='product',
            name='productGender',
            field=models.CharField(choices=[(True, 'kadın'), (False, 'erkek')], max_length=50, verbose_name='Ürünün Cinsiyeti'),
        ),
    ]
