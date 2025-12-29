from models.product import Product

class PerishableProduct(Product):
    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self.expiry_date = expiry_date

    def is_expired(self, current_date):
        return current_date > self.expiry_date
