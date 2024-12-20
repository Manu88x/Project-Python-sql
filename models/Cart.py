import sqlite3
from db.connection import get_db_connection

class Cart:
    def __init__(self, cart_id, user_id, product_id, quantity):
        self.cart_id = cart_id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    @classmethod
    def add_to_cart(cls, user_id, product_id, quantity):
        """Add a product to the user's cart."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Carts (UserId, ProductId, Quantity) VALUES (?, ?, ?)", 
                           (user_id, product_id, quantity))
            conn.commit()
            print("Product added to cart successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while adding to the cart: {e}")
        finally:
            conn.close()

    @classmethod
    def delete(cls, cart_id):
        """Delete an item from the cart by cart ID."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Carts WHERE Id = ?", (cart_id,))
            conn.commit()
            print("Cart item deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting the cart item: {e}")
        finally:
            conn.close()

    @classmethod
    def view_all(cls):
        """Retrieve and return a list of all cart items."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, UserId, ProductId, Quantity FROM Carts")
            rows = cursor.fetchall()
            return [cls(row[0], row[1], row[2], row[3]) for row in rows]  # cart_id, user_id, product_id, quantity
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving cart items: {e}")
            return []
        finally:
            conn.close()

    @classmethod
    def search(cls, user_id):
        """Search for cart items by user ID."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, UserId, ProductId, Quantity FROM Carts WHERE UserId = ?", (user_id,))
            rows = cursor.fetchall()
            return [cls(row[0], row[1], row[2], row[3]) for row in rows]  # cart_id, user_id, product_id, quantity
        except sqlite3.Error as e:
            print(f"An error occurred while searching for cart items: {e}")
            return []
        finally:
            conn.close()

    @classmethod
    def update(cls, cart_id, quantity):
        """Update the quantity of a specific item in the cart."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Carts SET Quantity = ? WHERE Id = ?", (quantity, cart_id))
            conn.commit()
            print("Cart item updated successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while updating the cart item: {e}")
        finally:
            conn.close()

    def __repr__(self):
        """Return a string representation of the cart item."""
        return f"Cart(CartId={self.cart_id}, UserId={self.user_id}, ProductId={self.product_id}, Quantity={self.quantity})"