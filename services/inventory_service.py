# services/inventory_service.py
from utils.database import execute_query, fetch_query


class InventoryService:


   def add_product(self, product, supplier_id=None):
       # Business validation
       if product.quantity < 0:
           raise ValueError("Quantity cannot be negative")


       if product.price <= 0:
           raise ValueError("Price must be greater than 0")


       expiry = getattr(product, "expiry_date", None)
       type_ = "perishable" if expiry else "regular"


       query = """
       INSERT INTO products (name, price, quantity, expiry_date, type, supplier_id)
       VALUES (%s, %s, %s, %s, %s, %s)
       RETURNING product_id;
       """


       result = execute_query(
           query,
           (product.name, product.price, product.quantity, expiry, type_, supplier_id),
           fetchone=True
       )


       product.product_id = result[0]
       return product


   def update_stock(self, product_id, quantity):
       if quantity < 0:
           raise ValueError("Stock quantity cannot be negative")


       query = """
       UPDATE products
       SET quantity=%s
       WHERE product_id=%s
       """
       execute_query(query, (quantity, product_id))


   def get_product(self, product_id):
       query = """
       SELECT product_id, name, price, quantity, expiry_date, type, supplier_id
       FROM products
       WHERE product_id=%s
       """
       result = fetch_query(query, (product_id,))
       return result[0] if result else None


   def list_products(self):
       query = """
       SELECT product_id, name, price, quantity, expiry_date, type
       FROM products
       ORDER BY product_id
       """
       return fetch_query(query)
