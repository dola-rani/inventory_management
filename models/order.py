class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity
        self.status = "Pending"

    def process_order(self):
        self.product.reduce_stock(self.quantity)
        self.status = "Completed"

    def __str__(self):
        return f"Order {self.order_id} | Product: {self.product.name} | Quantity: {self.quantity} | Status: {self.status}"
