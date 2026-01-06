class ReportService:
    def __init__(self, inventory_service):
        self.inventory_service = inventory_service

    def total_inventory_value(self):
        total = 0
        for product in self.inventory_service.list_products():
            total += product.price * product.quantity
        return total

    def low_stock_products(self, threshold):
        return [
            product
            for product in self.inventory_service.list_products()
            if product.quantity < threshold
        ]
