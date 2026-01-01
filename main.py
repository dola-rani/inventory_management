from models.product import Product
from models.order import Order
from services.inventory_service import InventoryService
from services.order_service import OrderService
from services.report_service import ReportService

inventory = InventoryService()
order_service = OrderService()
report_service = ReportService()

p1 = Product(1, "Laptop", 75000, 10)
p2 = Product(2, "Mouse", 1200, 3)

inventory.add_product(p1)
inventory.add_product(p2)

order = Order(101, p1, 2)
order_service.place_order(order)

print(order)

low_stock = report_service.low_stock_report(inventory.list_products(), 5)
print("\nLow stock items:")
for item in low_stock:
    print(item)
