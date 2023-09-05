from django.urls import path, include

from . import views
from accounts import views as AccountView

urlpatterns = [
    path("", AccountView.vendorDashboard, name="vendor"),
    path("profile/", views.vprofile, name="vprofile"),
    path("menu_builder/", views.menu_builder, name="menu_builder"),
    path(
        "menu_builder/catgory/<int:pk>/",
        views.fooditem_by_category,
        name="fooditem_by_category",
    ),
    # Category CRUD
    path("menu_builder/category/add/", views.add_category, name="add_category"),
    path(
        "menu_builder/category/edit/<int:pk>/",
        views.edit_category,
        name="edit_category",
    ),
    path(
        "menu_builder/category/delete/<int:pk>/",
        views.delete_category,
        name="delete_category",
    ),
    # FoodItem CRUD
    path("menu_builder/food/add/", views.add_food, name="add_food"),
    path(
        "menu_builder/food/edit/<int:pk>/",
        views.edit_food,
        name="edit_food",
    ),
    path(
        "menu_builder/food/delete/<int:pk>/",
        views.delete_food,
        name="delete_food",
    ),
]
