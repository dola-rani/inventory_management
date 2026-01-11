class ReportService:
   def __init__(self, inventory_service):
       self.inventory_service = inventory_service


   def total_inventory_value(self):
       total = 0
       for p in self.inventory_service.list_products():
           total += p['price'] * p['quantity']
       return total


   def low_stock_products(self, threshold):
       return [p for p in self.inventory_service.list_products() if p['quantity'] <= threshold]
