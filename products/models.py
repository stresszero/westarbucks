from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'menu'


class DrinkCategories(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'drink_categories'


class Drinks(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('DrinkCategories', on_delete=models.CASCADE)
    is_new = models.BooleanField(default=False)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'drinks'


class DrinkImages(models.Model):
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=3000)

    class Meta:
        db_table = 'drink_images'


class DrinkNutritions(models.Model):
    drink = models.OneToOneField('Drinks', on_delete=models.CASCADE)
    kcal = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sugar = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    protein = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sodium = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    fat = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    caffeine = models.DecimalField(max_digits=5, decimal_places=1, null=True)

    class Meta:
        db_table = 'drink_nutritions'


class Allergen(models.Model):
    name = models.CharField(max_length=100)
    drink = models.ManyToManyField('Drinks', through='DrinkAllergies')

    class Meta:
        db_table = 'allergen'


class DrinkAllergies(models.Model):
    drink = models.ForeignKey('Drinks', on_delete=models.CASCADE)
    allergen = models.ForeignKey('Allergen', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drink_allergies'
