from utils.database import execute_query, fetch_query
from models.supplier import Supplier
class SupplierService:
   def add_supplier(self, supplier):
       # Business validation

       if not supplier.name or not supplier.name.strip():
           raise ValueError("Supplier name is required")

       if not supplier.contact or not supplier.contact.strip():
           raise ValueError("Supplier contact is required")

       # Prevent duplicate suppliers (business rule)
       existing = fetch_query(
           "SELECT supplier_id FROM suppliers WHERE name=%s",
           (supplier.name,)
       )
       if existing:
           raise ValueError("Supplier already exists")


       query = """
       INSERT INTO suppliers (name, contact)
       VALUES (%s, %s)
       RETURNING supplier_id;
       """

       result = execute_query(
           query,
           (supplier.name.strip(), supplier.contact.strip()),
           fetchone=True
       )

       supplier.supplier_id = result[0]
       return supplier


   def list_suppliers(self):
       query = """
       SELECT supplier_id, name, contact
       FROM suppliers
       ORDER BY supplier_id
       """
       return fetch_query(query)


   def get_supplier(self, supplier_id):
       query = """
       SELECT supplier_id, name, contact
       FROM suppliers
       WHERE supplier_id=%s
       """
       result = fetch_query(query, (supplier_id,))
       return result[0] if result else None
import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection():
   return psycopg2.connect(
       host="localhost",
       database="inventory_db",
       user="postgres",
       password="root",
       port=8080 # Change only if your DB uses another port
   )


def execute_query(query, params=None, fetchone=False):
   conn = get_connection()
   try:
       with conn.cursor() as cur:
           cur.execute(query, params)
           if fetchone:
               result = cur.fetchone()
               conn.commit()
               return result
           conn.commit()
   finally:
       conn.close()


def fetch_query(query, params=None):
   conn = get_connection()
   try:
       with conn.cursor(cursor_factory=RealDictCursor) as cur:
           cur.execute(query, params)
           return cur.fetchall()
   finally:
       conn.close()
def validate_positive_int(value, field_name, allow_none=False):
   # It Allows None for DB-generated IDs
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