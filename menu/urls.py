from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('<int:menu_id>/', views.menu_item, name='menu_item'),
]
