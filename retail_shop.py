"""A small command-line retail shop system for learning Python and OOP."""

import sys


class Product:
    """A product with protected price and stock values."""

    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id.strip()
        self.name = name.strip()
        self.category = category.strip()
        self._price = float(price)
        self._quantity = int(quantity)

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def display_info(self):
        print(
            f"{self.product_id:<10} {self.name:<22} {self.category:<16} "
            f"₦{self.price:>10,.2f} {self.quantity:>8}"
        )

    def stock_value(self):
        return self.price * self.quantity

    def is_low_stock(self):
        return self.quantity < 5

    def reduce_stock(self, amount):
        if amount <= 0 or amount > self.quantity:
            return False
        self._quantity -= amount
        return True


class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.total_revenue = 0.0
        self.sales_history = []

    def find_product(self, product_id):
        wanted_id = product_id.strip().casefold()
        for product in self.products:
            if product.product_id.casefold() == wanted_id:
                return product
        return None

    def register_product(self, product):
        if self.find_product(product.product_id):
            return False
        self.products.append(product)
        return True

    def display_products(self, products=None):
        items = self.products if products is None else products
        if not items:
            print("No products to display.")
            return
        print(f"{'ID':<10} {'NAME':<22} {'CATEGORY':<16} {'UNIT PRICE':>11} {'STOCK':>8}")
        print("-" * 72)
        for product in items:
            product.display_info()

    def search_product(self, product_id):
        product = self.find_product(product_id)
        if product:
            self.display_products([product])
        else:
            print("Product not found.")

    def filter_by_category(self, category):
        matches = [p for p in self.products if p.category.casefold() == category.strip().casefold()]
        self.display_products(matches)

    def low_stock_products(self):
        return [product for product in self.products if product.is_low_stock()]

    def sell_product(self, product_id, quantity):
        product = self.find_product(product_id)
        if product is None:
            print("Sale failed: product not found.")
            return False
        if quantity <= 0:
            print("Sale failed: quantity must be greater than zero.")
            return False
        if quantity > product.quantity:
            print(f"Sale failed: only {product.quantity} item(s) are in stock.")
            return False

        amount = product.price * quantity
        product.reduce_stock(quantity)
        self.total_revenue += amount
        sale = {
            "product_id": product.product_id,
            "product_name": product.name,
            "quantity": quantity,
            "unit_price": product.price,
            "total": amount,
        }
        self.sales_history.append(sale)
        print("\n========== RECEIPT ==========")
        print(f"Product:     {product.name}")
        print(f"Quantity:    {quantity}")
        print(f"Unit price:  ₦{product.price:,.2f}")
        print(f"Total:       ₦{amount:,.2f}")
        print("=============================\n")
        return True

    def display_sales_history(self):
        if not self.sales_history:
            print("No completed sales yet.")
            return
        print(f"{'#':<5} {'PRODUCT':<22} {'QTY':>6} {'UNIT PRICE':>15} {'TOTAL':>15}")
        print("-" * 68)
        for number, sale in enumerate(self.sales_history, start=1):
            print(
                f"{number:<5} {sale['product_name']:<22} {sale['quantity']:>6} "
                f"₦{sale['unit_price']:>13,.2f} ₦{sale['total']:>13,.2f}"
            )

    def business_report(self):
        units_left = sum(product.quantity for product in self.products)
        stock_value = sum(product.stock_value() for product in self.products)
        low_stock = self.low_stock_products()
        print(f"\n========== {self.name.upper()} BUSINESS REPORT ==========")
        print(f"Registered products:       {len(self.products)}")
        print(f"Completed sales:           {len(self.sales_history)}")
        print(f"Total units remaining:     {units_left}")
        print(f"Value of remaining stock:  ₦{stock_value:,.2f}")
        print(f"Total revenue:             ₦{self.total_revenue:,.2f}")
        print("Products needing restock:")
        if low_stock:
            for product in low_stock:
                print(f"  - {product.name} (ID: {product.product_id}, stock: {product.quantity})")
        else:
            print("  None")
        print("=" * (len(self.name) + 32) + "\n")


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def read_integer(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a whole number of at least {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def read_price(prompt):
    while True:
        try:
            value = float(input(prompt).replace(",", ""))
            if value <= 0:
                print("Price must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid price, such as 2000 or 1999.50.")


def register_product(shop):
    print("\n--- Register product ---")
    product_id = read_non_empty("Product ID: ")
    if shop.find_product(product_id):
        print("That product ID is already registered.")
        return
    name = read_non_empty("Name: ")
    category = read_non_empty("Category: ")
    price = read_price("Unit price (₦): ")
    quantity = read_integer("Quantity in stock: ", minimum=0)
    shop.register_product(Product(product_id, name, category, price, quantity))
    print(f"{name} registered successfully.")


def print_menu():
    print("\n====== RETAIL SHOP MENU ======")
    print("1. Register a product")
    print("2. Display all products")
    print("3. Search for a product")
    print("4. Filter products by category")
    print("5. Sell a product")
    print("6. Display low-stock products")
    print("7. View sales history")
    print("8. Generate a business report")
    print("9. Exit")


def main():
    # The naira symbol is outside Windows' legacy cp1252 console encoding.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    shop = Shop("Everyday Retail Shop")
    starter_products = [
        Product("P001", "Long Grain Rice", "Grains", 75000, 20),
        Product("P002", "Bottled Water", "Beverages", 500, 40),
        Product("P003", "Soft Drink", "Beverages", 800, 3),
        Product("P004", "Cooking Oil", "Groceries", 6500, 12),
        Product("P005", "Bathing Soap", "Toiletries", 1200, 4),
    ]
    for product in starter_products:
        shop.register_product(product)

    print(f"Welcome to {shop.name}! Five sample products are ready to explore.")
    while True:
        print_menu()
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            register_product(shop)
        elif choice == "2":
            shop.display_products()
        elif choice == "3":
            shop.search_product(read_non_empty("Enter product ID: "))
        elif choice == "4":
            shop.filter_by_category(read_non_empty("Enter category: "))
        elif choice == "5":
            product_id = read_non_empty("Enter product ID: ")
            quantity = read_integer("Quantity to sell: ")
            shop.sell_product(product_id, quantity)
        elif choice == "6":
            shop.display_products(shop.low_stock_products())
        elif choice == "7":
            shop.display_sales_history()
        elif choice == "8":
            shop.business_report()
        elif choice == "9":
            print("Thank you for using the retail shop system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 9.")


if __name__ == "__main__":
    main()
