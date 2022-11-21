from django.urls import path

from shop import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("finish/success", views.payment_success_view, name="payment_success"),
    path("finish/failed", views.payment_failed_view, name="payment_failed"),
    path("buy/<int:item_id>", views.buy_view,name="buy"),
    path("item/<int:item_id>", views.item_view, name="item"),
]
