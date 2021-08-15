from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table='menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table='categories'

class Product(models.Model):
    kor_name = models.CharField(max_length=20)
    eng_name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    nutrition = models.ForeignKey('Nutrition', on_delete=models.CASCADE)

    class Meta:
        db_table='products'

class Image(models.Model):
    imgae_url = models.CharField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table='images'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    saturated_fat_g = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    sugars_g = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    protein_g = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    caffeine_mg = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    size_ml = models.CharField(max_length=45,null=True)
    size_fluid_ounce = models.CharField(max_length=45,null=True)

    class Meta:
        db_table='nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    product = models.ManyToManyField('Product', through='AllergyProduct')

    class Meta:
        db_table='allergy'
    
class AllergyProduct(models.Model):
    allaergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table='allergy_products'
