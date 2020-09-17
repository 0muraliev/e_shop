# Generated by Django 3.0.8 on 2020-08-27 10:46

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200812_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.Category', verbose_name='Родитель'),
        ),
    ]