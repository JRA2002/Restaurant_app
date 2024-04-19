from django.contrib import admin
from .models import Ingredient,MenuItem,RecipeRequirements,Order
# Register your models here.
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirements)



