from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from shop.models import Item
from shop.services.stripe import create_stripe_session


def item_view(request, item_id: int) -> HttpResponse:
    item = get_object_or_404(Item, pk=item_id)
    return render(
        request,
        "item.html",
        context={
            "item": item,
            "endpoint": f"/buy/{item_id}",
            "stripe_api_pk": settings.STRIPE_API_PUBLISHABLE_KEY,
        },
    )


def buy_view(_, item_id: int) -> JsonResponse:
    item = get_object_or_404(Item, pk=item_id)
    stripe_session = create_stripe_session(
        secret_key=settings.STRIPE_API_SECRET_KEY,
        success_url="http://0.0.0.0:8000/finish/success",
        cancel_url="http://0.0.0.0:8000/finish/failed",
        product_name=str(item),
        price=item.price,
        quantity=1,
        currency="usd",
    )
    return JsonResponse(
        {"stripe_session_id": stripe_session.stripe_id}
    )


def index_view(request) -> HttpResponse:
    items = Item.objects.order_by("item_id")
    return render(request, "index.html", context={"items": items})


def payment_failed_view(request) -> HttpResponse:
    return render(request, "payment_failed.html")


def payment_success_view(request) -> HttpResponse:
    return render(request, "payment_success.html")
