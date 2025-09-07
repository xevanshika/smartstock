import json
import os

# ---------------------------
# File to store data
# ---------------------------
DATA_FILE = "inventory.json"

# ---------------------------
# Load / Save Functions
# ---------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"products": {}, "sales": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------------------
# Inventory Functions
# ---------------------------
def add_product(data):
    pid = input("Enter Product ID: ")
    if pid in data["products"]:
        print("❌ Product already exists!")
        return
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))
    data["products"][pid] = {"name": name, "price": price, "qty": qty}
    print(f"✅ Product '{name}' added successfully!")

def view_products(data):
    if not data["products"]:
        print("No products in inventory!")
        return
    print("\n--- Inventory ---")
    for pid, details in data["products"].items():
        print(f"ID: {pid} | Name: {details['name']} | Price: {details['price']} | Qty: {details['qty']}")

def remove_product(data):
    pid = input("Enter Product ID to remove: ")
    if pid in data["products"]:
        del data["products"][pid]
        print("✅ Product removed successfully!")
    else:
        print("❌ Product not found!")

def update_stock(data):
    pid = input("Enter Product ID to update: ")
    if pid in data["products"]:
        qty = int(input("Enter quantity to add: "))
        data["products"][pid]["qty"] += qty
        print("✅ Stock updated!")
    else:
        print("❌ Product not found!")

# ---------------------------
# Sales Functions
# ---------------------------
def create_order(data):
    pid = input("Enter Product ID to buy: ")
    if pid not in data["products"]:
        print("❌ Product not found!")
        return
    qty = int(input("Enter quantity: "))
    if qty > data["products"][pid]["qty"]:
        print("❌ Not enough stock!")
        return
    # Update stock
    data["products"][pid]["qty"] -= qty
    total = qty * data["products"][pid]["price"]
    order = {
        "product_id": pid,
        "name": data["products"][pid]["name"],
        "qty": qty,
        "total": total
    }
    data["sales"].append(order)
    print(f"✅ Order placed! Bill Amount = {total}")

def view_sales(data):
    if not data["sales"]:
        print("No sales yet!")
        return
    print("\n--- Sales Report ---")
    total_revenue = 0
    for order in data["sales"]:
        print(f"Product: {order['name']} | Qty: {order['qty']} | Amount: {order['total']}")
        total_revenue += order["total"]
    print(f"Total Revenue: {total_revenue}")

# ---------------------------
# Main Menu
# ---------------------------
def main():
    data = load_data()
    while True:
        print("\n--- Inventory & Sales Management ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Remove Product")
        print("4. Update Stock")
        print("5. Create Order (Sale)")
        print("6. View Sales Report")
        print("7. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_product(data)
        elif choice == "2":
            view_products(data)
        elif choice == "3":
            remove_product(data)
        elif choice == "4":
            update_stock(data)
        elif choice == "5":
            create_order(data)
        elif choice == "6":
            view_sales(data)
        elif choice == "7":
            save_data(data)
            print("Data saved! Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
