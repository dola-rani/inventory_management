from utils.database import execute_query, get_connection


class OrderService:


   def place_order(self, order):
       # Validate quantity
       if order.quantity <= 0:
           print("Quantity must be greater than 0")
           return False


       # Check stock availability
       if order.quantity > order.product.quantity:
           print("Insufficient stock")
           print(f"Available stock: {order.product.quantity}")
           return False


       conn = get_connection()
       try:
           with conn.cursor() as cur:
               # Reduce stock in memory
               order.product.reduce_stock(order.quantity)
               order.status = "COMPLETED"


               # Update product stock
               cur.execute(
                   "UPDATE products SET quantity=%s WHERE product_id=%s",
                   (order.product.quantity, order.product.product_id)
               )


               # Insert order record
               cur.execute(
                   """
                   INSERT INTO orders (product_id, quantity, status)
                   VALUES (%s, %s, %s)
                   """,
                   (
                       order.product.product_id,
                       order.quantity,
                       order.status
                   )
               )


           conn.commit()
           print("Order placed successfully")
           return True


       except Exception as e:
           conn.rollback()
           print("Order failed:", e)
           return False


       finally:
           conn.close()
