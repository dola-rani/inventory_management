**Inventory Management System**

A console-based inventory management system built with Python and PostgreSQL.
This system allows managing products (regular & perishable), suppliers, orders, and inventory reports via an interactive CLI (Command-Line Interface).

Features

1. Supplier Management
  a. Add new suppliers with validation.
  b. Prevent duplicate supplier entries.
  c. List all suppliers.

2. Product Management
  a. Add regular and perishable products.
  b. Link products to suppliers.
  c. Add or reduce stock with validation.
  d. Prevent negative stock.
  e.Show inventory with supplier info and expiry date for perishable items.

3. Order Management
  a. Place orders for products.
  b. Validate stock availability.
  c. Automatically update product quantity.
  d. Track order status.

4. Reports
  a. Calculate total inventory value.
  b. Identify low-stock products based on a threshold.

5. CLI Interface
  a. Fully interactive command-line menu.
  b. Step-by-step input validation.
