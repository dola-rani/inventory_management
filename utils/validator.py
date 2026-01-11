def validate_positive_int(value, field_name, allow_none=False):
   # Allow None for DB-generated IDs
   if value is None:
       if allow_none:
           return
       raise TypeError(f"{field_name} cannot be None")

   if not isinstance(value, int):
       raise TypeError(f"{field_name} must be an integer")
   if value <= 0:
       raise ValueError(f"{field_name} must be greater than zero")


def validate_price(price):
   if not isinstance(price, (int, float)):
       raise TypeError("Price must be a number")
   if price <= 0:
       raise ValueError("Price must be greater than zero")


def validate_string(value, field_name):
   if not isinstance(value, str) or not value.strip():
       raise ValueError(f"{field_name} must be a non-empty string")
