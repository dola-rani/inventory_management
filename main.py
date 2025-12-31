from models.product import Product
from models.perishable_product import PerishableProduct
from models.supplier import Supplier
from models.order import Order
p1 = Product(1, "MacBook", 220000, 10)
p1.add_stock(7)
p1.reduce_stock(2)
print(p1)

p2 = PerishableProduct(2, "Drinks", 80, 20, "2025-01-10")
print(f"{p2.name} expired? {p2.is_expired('2025-01-11')}")


s1 = Supplier(1, "ABC Traders", "0123456789")
print(s1)


order1 = Order(101, p1, 2)
order1.process_order()
print(order1)
print(p1)  # Check updated stock
