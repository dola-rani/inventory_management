class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount

    def reduce_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Insufficient stock")
        self.quantity -= amount

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Stock: {self.quantity}"
