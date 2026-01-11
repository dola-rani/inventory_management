from utils.validator import validate_string


class Supplier:
   def __init__(self, supplier_id, name, contact=None):
       if supplier_id is not None:
           if not isinstance(supplier_id, int) or supplier_id <= 0:
               raise ValueError("Supplier ID must be a positive integer")
       validate_string(name, "Supplier name")
       self.supplier_id = supplier_id
       self.name = name
       self.contact = contact


   def __str__(self):
       return f"{self.name} | Contact: {self.contact}"