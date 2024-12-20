from models.Customer import Customer
from models.Product import Product
from models.Cart import Cart

def main_menu():
    print("\n--- Welcome to the E-Commerce Management System ---")
    print("Manage Customers, Products, and Shopping Carts with ease.")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add (Customer/Product/Cart)")
        print("2. Delete (Customer/Product/Cart)")
        print("3. View All Customers")
        print("4. Search Customer")
        print("5. Update Customer")
        print("6. View All Products")
        print("7. Search Product")
        print("8. Update Product")
        print("9. View All Carts")
        print("10. Search Cart")
        print("11. Update Cart")
        print("12. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            entity = input("Do you want to add a (1)ustomer, (2)roduct, or (3)art item? ").strip().upper()
            if entity == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                Customer.create(name, email, password)
            elif entity == '2':
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                Product.create(name, price, quantity)
            elif entity == '3':
                user_id = int(input("Enter user ID: "))
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))
                Cart.add_to_cart(user_id, product_id, quantity)
            else:
                print("Invalid action. Please choose 1, 2, or 3.")
        
        elif choice == '2':
            entity = input("Do you want to delete a (1)ustomer, (2)roduct, or (3)art item? ").strip().upper()
            if entity == '1':
                user_id = int(input("Enter user ID to delete: "))
                Customer.delete(user_id)
            elif entity == '2':
                product_id = int(input("Enter product ID to delete: "))
                Product.delete(product_id)
            elif entity == '3':
                cart_id = int(input("Enter cart ID to delete: "))
                Cart.delete(cart_id)
            else:
                print("Invalid action. Please choose 1, 2, or 3.")
        
        elif choice == '3':
            customers = Customer.view_all()
            for customer in customers:
                print(customer)
        
        elif choice == '4':
            email = input("Enter email to search: ")
            customer = Customer.search(email)
            print(customer if customer else "Customer not found.")
        
        elif choice == '5':
            user_id = int(input("Enter user ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            password = input("Enter new password (leave blank to skip): ")
            Customer.update(user_id, name or None, email or None, password or None)
        
        elif choice == '6':
            products = Product.view_all()
            for product in products:
                print(product)
        
        elif choice == '7':
            name = input("Enter product name to search: ")
            product = Product.search(name)
            print(product if product else "Product not found.")
        
        elif choice == '8':
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            price = input("Enter new price (leave blank to skip): ")
            quantity = input("Enter new quantity (leave blank to skip): ")
            Product.update(product_id, name or None, float(price) if price else None, int(quantity) if quantity else None)
        
        elif choice == '9':
            carts = Cart.view_all()
            for cart in carts:
                print(cart)
        
        elif choice == '10':
            user_id = int(input("Enter user ID to search for cart: "))
            cart_items = Cart.search(user_id)
            if cart_items:
                for item in cart_items:
                    print(item)
            else:
                print("No cart items found for this user.")
        
        elif choice == '11':
            cart_id = int(input("Enter cart ID to update: "))
            quantity = int(input("Enter new quantity: "))
            Cart.update(cart_id, quantity)
        
        elif choice == '12':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()