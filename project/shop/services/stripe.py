import stripe


def create_stripe_session(secret_key: str, success_url: str, cancel_url: str, product_name: str, price: int,
                          quantity: int = 1, currency: str = "usd", ) -> stripe.checkout.Session:
    stripe.api_key = secret_key
    return stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": currency,
                    "product_data": {
                        "name": product_name,
                    },
                    "unit_amount": price,
                },
                "quantity": quantity,
            }
        ],
        success_url=success_url,
        cancel_url=cancel_url,
        mode="payment",
    )
