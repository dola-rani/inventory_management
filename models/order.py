from datetime import datetime

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.status = "Pending"
        self.created_at = datetime.now()
        self.completed_at = None

    def process_order(self):
        if self.quantity <= 0:
            raise ValueError("Order quantity must be greater than zero.")
        if self.product.quantity < self.quantity:
            raise ValueError(f"Insufficient stock for {self.product.name}. Available: {self.product.quantity}, Requested: {self.quantity}")
        self.product.reduce_stock(self.quantity)
        self.status = "Completed"
        self.completed_at = datetime.now()

    def __str__(self):
        completed_str = self.completed_at.strftime("%Y-%m-%d %H:%M:%S") if self.completed_at else "Not completed"
        return (f"Order {self.order_id} | Product: {self.product.name} | "
                f"Quantity: {self.quantity} | Status: {self.status} | "
                f"Created at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')} | "
                f"Completed at: {completed_str}")
