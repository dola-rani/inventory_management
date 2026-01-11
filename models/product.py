from utils.validator import validate_positive_int, validate_price, validate_string
class Product:
   def __init__(self, product_id, name, price, quantity):
       # Allow None for DB-generated IDs
       if product_id is not None:
           validate_positive_int(product_id, "Product ID")


       validate_string(name, "Product name")
       validate_price(price)
       validate_positive_int(quantity, "Quantity")


       self.product_id = product_id
       self.name = name
       self.price = price
       self.quantity = quantity


   def add_stock(self, amount):
       validate_positive_int(amount, "Stock amount")
       self.quantity += amount


   def reduce_stock(self, amount):
       validate_positive_int(amount, "Stock amount")
       if amount > self.quantity:
           raise ValueError("Insufficient stock")
       self.quantity -= amount


   def __str__(self):
       return f"{self.name} | Price: {self.price} | Stock: {self.quantity}"

