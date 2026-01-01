class InventoryService:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product not found")
        del self.products[product_id]

    def get_product(self, product_id):
        return self.products.get(product_id)

    def list_products(self):
        return self.products.values()
