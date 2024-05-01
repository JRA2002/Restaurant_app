from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Ingredient,MenuItem,RecipeRequirements,Order
from django.db.models import Sum
# Create your views here.

class HomView(TemplateView):
    template_name = "Restlima/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.all()
        revenue = Order.objects.aggregate(revenue=Sum('menu__menu_price'))['revenue']
        #ganancias==revenue
        #costo==total
        #total = ganncias - costo
    
        total_cost = 0
        
        for orders in Order.objects.all():
            for receta_requirements in orders.menu.reciperequirements_set.all():
                total_cost = total_cost + receta_requirements.quantity*receta_requirements.ingredients.unit_price
        context['revenue'] = revenue
        context['total_cost'] = total_cost
        context['total'] = revenue-total_cost
        
        return context
    
class MenuItemView(ListView):
    model = MenuItem
    template_name = "Restlima/menu.html"
    
class OrderView(ListView):
    model = Order
    template_name = "Restlima/order.html"
    

class casa(TemplateView):
    template_name = "Restlima/casa.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['casa'] = request.get_full_path_info()
        return context
        
    
        
        