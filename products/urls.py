from django.urls import path

from . import views

urlpatterns = [
    path("create", views.create_product_view),
    path("get_all", views.get_all_view),
    path("get_one", views.get_one_view),
    path("put", views.put_view),
]