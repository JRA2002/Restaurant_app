from django.db import models

# Create your models here.
CATEGORY = [
    ("Fruits","Fruits"),
    ("Vegetables","Vegetables"),
    ("Meat","Meat"),
    ("Dairy","Dairy"),
    ("Grains","Grains"),
]
class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(choices=CATEGORY,max_length=20)
    unit_price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    menu_name = models.CharField(max_length=20)
    menu_price = models.IntegerField(default=0)

    def __str__(self):
        return self.menu_name
    
    
    
class Order(models.Model):
    menu = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    
    def __str__(self):
        return str(self.menu)
    
    def total_price_order(self):
        return self.menu.menu_price*self.quantity
    
class RecipeRequirements(models.Model):
    menu = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.menu)