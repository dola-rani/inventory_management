from models.product import Product

p1 = Product(1, "Laptop", 75000, 10)
p1.add_stock(5)
p1.reduce_stock(3)

print(p1)
