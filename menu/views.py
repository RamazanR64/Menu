from django.shortcuts import render, get_object_or_404
from .models import MenuItem


def menu_item(request, menu_id):
    menu_item = get_object_or_404(MenuItem, id=menu_id)
    return render(request, 'menu/menu_item.html', {'menu_item': menu_item})
