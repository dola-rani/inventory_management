class OrderService:
    def place_order(self, order):
        if order.quantity <= 0:
            raise ValueError("Order quantity must be greater than zero")

        order.process_order()
        return order
