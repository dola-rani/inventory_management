from models.product import Product
from models.perishable_product import PerishableProduct
from models.order import Order
from models.supplier import Supplier
from services.inventory_service import InventoryService
from services.order_service import OrderService
from services.report_service import ReportService
from services.supplier_service import SupplierService



def select_supplier(supplier_service):
   suppliers = supplier_service.list_suppliers()
   if not suppliers:
       print("No suppliers found. Please add a supplier first.")
       return None


   print("\nSuppliers:")
   for s in suppliers:
       print(f"{s['supplier_id']}: {s['name']} | Contact: {s['contact']}")


   while True:
       try:
           supplier_id = int(input("Enter supplier ID for this product: "))
           if any(s['supplier_id'] == supplier_id for s in suppliers):
               return supplier_id
           else:
               print(" Invalid supplier ID. Try again.")
       except ValueError:
           print(" Please enter a valid number.")

def add_supplier_interactively(supplier_service):
   print("\n--- Add New Supplier ---")


   while True:
       name = input("Supplier Name: ").strip()
       contact = input("Supplier Contact: ").strip()

       if not name:
           print("Supplier name cannot be empty. Please enter a valid name.\n")
           continue
       if not contact:
           print("Supplier contact cannot be empty. Please enter a phone number or email.\n")
           continue


       # Prevent duplicate
       existing_suppliers = supplier_service.list_suppliers()
       if any(s['name'].lower() == name.lower() for s in existing_suppliers):
           print(f" Supplier '{name}' already exists. Please enter a different name.\n")
           continue


       try:
           supplier = Supplier(None, name, contact)
           supplier_service.add_supplier(supplier)
           print(f" Supplier '{name}' added successfully!")
           break
       except ValueError as e:
           print(f"  {e}. Please try again.\n")

def add_product_interactively(inventory_service, supplier_service):
   print("\n--- Add New Product ---")


   supplier_id = select_supplier(supplier_service)
   if supplier_id is None:
       return


   while True:
       try:
           name = input("Product Name: ").strip()
           if not name:
               print(" Product name cannot be empty. Please try again.")
               continue
           price_input = input("Price: ").strip()
           if not price_input:
               print("Price cannot be empty. Please try again.")
               continue
           price = float(price_input)
           if price <= 0:
               print(" Price must be greater than zero.")
               continue


           quantity_input = input("Quantity: ").strip()
           if not quantity_input:
               print("Quantity cannot be empty. Please try again.")
               continue
           quantity = int(quantity_input)
           if quantity < 0:
               print("Quantity cannot be negative.")
               continue


           product_type = input("Product Type (regular/perishable): ").lower().strip()
           if product_type == "perishable":
               expiry_date = input("Expiry Date (YYYY-MM-DD): ").strip()
               if not expiry_date:
                   print(" Expiry date cannot be empty for perishable products.")
                   continue
               product = PerishableProduct(None, name, price, quantity, expiry_date)
           elif product_type == "regular":
               product = Product(None, name, price, quantity)
           else:
               print(" Invalid product type. Choose 'regular' or 'perishable'.")
               continue


           inventory_service.add_product(product, supplier_id=supplier_id)
           print(f" Product '{name}' added successfully!")
           break


       except ValueError as e:
           print(f" {e}. Please try again.\n")


def place_order_interactively(order_service, inventory_service):
   print("\n--- Place New Order ---")


   products = inventory_service.list_products()
   if not products:
       print(" No products available to order.")
       return


   while True:
       print("\nProducts:")
       for p in products:
           print(f"{p['product_id']}: {p['name']} | Stock: {p['quantity']}")


       try:
           product_id_input = input("Enter product ID to order: ").strip()
           if not product_id_input:
               print(" Product ID cannot be empty.")
               continue
           product_id = int(product_id_input)

           product_data = next((p for p in products if p['product_id'] == product_id), None)
           if not product_data:
               print(" Invalid product ID.")
               continue


           while True:
               quantity_input = input("Enter quantity to order: ").strip()
               if not quantity_input:
                   print(" Quantity cannot be empty.")
                   continue
               quantity = int(quantity_input)
               if quantity <= 0:
                   print(" Quantity must be greater than zero.")
                   continue


               if quantity > product_data['quantity']:
                   print(f" Insufficient stock. Available: {product_data['quantity']}")
                   print("1. Retry quantity")
                   print("2. Choose another product")
                   print("3. Cancel order")
                   choice = input("Choose: ").strip()
                   if choice == "1":
                       continue
                   elif choice == "2":
                       break  # back to product selection
                   else:
                       print(" Order cancelled.")
                       return

               # Convert price to float to fix Decimal error
               product_obj = Product(
                   product_data['product_id'],
                   product_data['name'],
                   float(product_data['price']),
                   product_data['quantity']
               )

               order = Order(None, product_obj, quantity)
               order_service.place_order(order)
               print(f" Order placed: {product_data['name']} x {quantity}")
               return


       except ValueError:
           print(" Please enter valid numbers.")

def main():
   supplier_service = SupplierService()
   inventory_service = InventoryService()
   order_service = OrderService()
   report_service = ReportService(inventory_service)


   while True:
       print("\n--- Inventory Management Menu ---")
       print("1. Add Supplier")
       print("2. Add Product")
       print("3. Place Order")
       print("4. Show Inventory")
       print("5. Show Reports")
       print("6. Exit")
       choice = input("Enter your choice: ").strip()
       if choice == "1":
           add_supplier_interactively(supplier_service)
       elif choice == "2":
           add_product_interactively(inventory_service, supplier_service)
       elif choice == "3":
           place_order_interactively(order_service, inventory_service)
       elif choice == "4":
           products = inventory_service.list_products()
           if not products:
               print("Inventory is empty.")
           else:
               print("\n--- Inventory ---")
               for p in products:
                   supplier = supplier_service.get_supplier(p.get('supplier_id'))
                   supplier_name = supplier['name'] if supplier else "N/A"
                   expiry = f"| Expiry: {p['expiry_date']}" if p.get('expiry_date') else ""
                   print(f"{p['name']} | Price: {p['price']} | Stock: {p['quantity']} | Supplier: {supplier_name} {expiry}")
       elif choice == "5":
           print("\n--- Reports ---")
           print("Total Inventory Value:", report_service.total_inventory_value())
           low_stock = report_service.low_stock_products(5)
           print("Low Stock Products:", [p['name'] for p in low_stock])

       elif choice == "6":
           print("Exiting program...")
           break

       else:
           print("Invalid choice. Try again.")


if __name__ == "__main__":
   main()

