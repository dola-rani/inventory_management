from datetime import datetime
from models.product import Product


class PerishableProduct(Product):
   def __init__(self, product_id, name, price, quantity, expiry_date):
       super().__init__(product_id, name, price, quantity)


       # Convert expiry_date to datetime date
       if isinstance(expiry_date, str):
           try:
               expiry_dt = datetime.strptime(expiry_date, "%Y-%m-%d").date()
           except ValueError:
               raise ValueError("Expiry date must be in YYYY-MM-DD format")
       elif isinstance(expiry_date, datetime):
           expiry_dt = expiry_date.date()
       else:
           raise TypeError("Expiry date must be a string or datetime object")


       # Check expiry is today or in the future
       today = datetime.now().date()
       if expiry_dt < today:
           raise ValueError(f"Expiry date {expiry_dt} cannot be in the past (today is {today})")
       self.expiry_date = expiry_dt


   def __str__(self):
       return f"{self.name} | Price: {self.price} | Stock: {self.quantity} | Expiry: {self.expiry_date}"
