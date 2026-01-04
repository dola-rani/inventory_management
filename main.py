from models.product import Product
from models.perishable_product import PerishableProduct
from models.order import Order
from services.inventory_service import InventoryService
from services.order_service import OrderService
from services.report_service import ReportService


def main():
    # Initialize services
    inventory_service = InventoryService()
    order_service = OrderService()
    report_service = ReportService(inventory_service)

    # Create products
    iphone = Product(
        product_id=1,
        name="iPhone",
        price=180000,
        quantity=10
    )

    milk = PerishableProduct(
        product_id=2,
        name="Milk",
        price=80,
        quantity=20,
        expiry_date="2026-01-04"
    )

    # Add products to inventory
    inventory_service.add_product(iphone)
    inventory_service.add_product(milk)

    # Place a valid order
    order = Order(
        order_id=101,
        product=iphone,
        quantity=2
    )
    order_service.place_order(order)

    # Display inventory
    print("\n Inventory Products:")
    for product in inventory_service.list_products():
        print(product)

    # Generate reports
    print("\n Inventory Reports:")
    print("Total Inventory Value:", report_service.total_inventory_value())
    print("Low Stock Products:", report_service.low_stock_products(threshold=5))


if __name__ == "__main__":
    main()
