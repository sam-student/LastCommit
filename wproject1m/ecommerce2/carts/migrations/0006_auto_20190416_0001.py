# Generated by Django 2.0 on 2019-04-15 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_knowledge_score'),
        ('carts', '0005_cart_accessory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ManyToManyField(blank=True, to='product.Product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='carts.CartItem'),
        ),
    ]
