# Generated by Django 3.2.6 on 2021-08-15 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('size_ml', models.CharField(max_length=45, null=True)),
                ('size_fluid_ounce', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kor_name', models.CharField(max_length=20)),
                ('eng_name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.nutrition')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgae_url', models.CharField(max_length=2000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.CreateModel(
            name='AllergyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allaergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'allergy_products',
            },
        ),
        migrations.AddField(
            model_name='allergy',
            name='product',
            field=models.ManyToManyField(through='products.AllergyProduct', to='products.Product'),
        ),
    ]
