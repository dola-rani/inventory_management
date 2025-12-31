class Supplier:
    def __init__(self, supplier_id, name, contact):
        self.supplier_id = supplier_id
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"{self.name} | Contact: {self.contact}"

