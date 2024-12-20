import sqlite3
from db.connection import get_db_connection

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def create(cls, name, price, quantity):
        """Add a new product to the database."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Products (Name, Price, Quantity) VALUES (?, ?, ?)", 
                           (name, price, quantity))
            conn.commit()
            print("Product added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while adding the product: {e}")
        finally:
            conn.close()

    @classmethod
    def delete(cls, product_id):
        """Delete a product from the database by product ID."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Products WHERE Id = ?", (product_id,))
            conn.commit()
            print("Product deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting the product: {e}")
        finally:
            conn.close()

    @classmethod
    def view_all(cls):
        """Retrieve and return a list of all products."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, Name, Price, Quantity FROM Products")
            rows = cursor.fetchall()
            return [cls(row[0], row[1], row[2], row[3]) for row in rows]  # product_id, name, price, quantity
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving products: {e}")
            return []
        finally:
            conn.close()

    @classmethod
    def search(cls, name):
        """Search for a product by name."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, Name, Price, Quantity FROM Products WHERE Name = ?", (name,))
            row = cursor.fetchone()
            return cls(row[0], row[1], row[2], row[3]) if row else None  # product_id, name, price, quantity
        except sqlite3.Error as e:
            print(f"An error occurred while searching for the product: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def update(cls, product_id, name=None, price=None, quantity=None):
        """Update product details."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            if name:
                cursor.execute("UPDATE Products SET Name = ? WHERE Id = ?", (name, product_id))
            if price is not None:  # Allow price to be updated to 0
                cursor.execute("UPDATE Products SET Price = ? WHERE Id = ?", (price, product_id))
            if quantity is not None:  # Allow quantity to be updated to 0
                cursor.execute("UPDATE Products SET Quantity = ? WHERE Id = ?", (quantity, product_id))
            conn.commit()
            print("Product updated successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while updating the product: {e}")
        finally:
            conn.close()

    def __repr__(self):
        """Return a string representation of the product."""
        return f"Product(Id={self.product_id}, Name='{self.name}', Price={self.price}, Quantity={self.quantity})"