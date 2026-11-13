from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_view),
    path("", views.create_product_view),
]