import os
import django
from django.db.models import Count, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Order, Product


# Import your models here
# Create and run your queries within functions


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    searched_profiles = Profile.objects.prefetch_related(
        "orders"
    ).annotate(
        num_orders=Count("orders")
    ).filter(
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    ).order_by("full_name")

    if not searched_profiles:
        return ""

    return "\n".join(f"Profile: {profile.full_name}, "
                     f"email: {profile.email}, "
                     f"phone number: {profile.phone_number}, "
                     f"orders: {profile.num_orders}"
                     for profile in searched_profiles)


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()

    if not loyal_profiles:
        return ""

    return "\n".join(f"Profile: {profile.full_name}, orders: {profile.num_orders}" for profile in loyal_profiles)


def get_last_sold_products():
    last_order = Order.objects.prefetch_related("products").last()

    if not last_order or not last_order.products.all():
        return ""

    products = ", ".join([product.name for product in last_order.products.order_by("name")])

    return f"Last sold products: {products}"


def get_top_products():
    top_products = Product.objects.prefetch_related(
        "orders"
    ).annotate(
        num_ordered=Count("orders")
    ).filter(
        num_ordered__gt=0
    ).order_by(
        "-num_ordered", "name"
    )[:5]

    if not top_products or not top_products[0].orders.all():
        return ""

    products = "\n".join(f"{product.name}, sold {product.num_ordered} times" for product in top_products)

    return f"Top products:\n{products}"


def apply_discounts():
    orders_for_discount = Order.objects.prefetch_related(
        "products"
    ).annotate(
        num_products=Count("products")
    ).filter(
        is_completed=False,
        num_products__gt=2
    )

    num_of_updated_orders = orders_for_discount.update(total_price=F("total_price") * 0.9) if orders_for_discount else 0

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():

    order_for_complete = Order.objects.prefetch_related("products").filter(is_completed=False).first()

    if not order_for_complete:
        return ""

    order_for_complete.is_completed = True
    order_for_complete.save()

    for product in order_for_complete.products.all():
        product.in_stock -= 1
        if product.in_stock == 0:
            product.is_available = False
        product.save()

    return "Order has been completed!"


print(get_top_products())
