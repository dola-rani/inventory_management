class ReportService:
    def low_stock_report(self, products, threshold=5):
        low_stock_items = []

        for product in products:
            if product.quantity <= threshold:
                low_stock_items.append(product)

        return low_stock_items
