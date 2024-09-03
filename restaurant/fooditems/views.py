from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItems
# Create your views here.


def addItem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        items = request.POST.get('items')
        foodtype = request.POST.get("foodtype")
        price = request.POST.get('price')
        FoodItems.object.create(
            name=name,
            items=items,
            foodtype=foodtype,
            price=price

        )
    return render(request,'pen.html')