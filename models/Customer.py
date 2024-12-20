import sqlite3
from db.connection import get_db_connection

class Customer:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def create(cls, name, email, password):
        """Add a new customer to the database."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Users (Name, Email, Password) VALUES (?, ?, ?)", 
                           (name, email, password))
            conn.commit()
            print("Customer added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while adding the customer: {e}")
        finally:
            conn.close()

    @classmethod
    def delete(cls, user_id):
        """Delete a customer from the database by user ID."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Users WHERE Id = ?", (user_id,))
            conn.commit()
            print("Customer deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while deleting the customer: {e}")
        finally:
            conn.close()

    @classmethod
    def view_all(cls):
        """Retrieve and return a list of all customers."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, Name, Email FROM Users")
            rows = cursor.fetchall()
            return [cls(row[0], row[1], row[2], None) for row in rows]  # user_id, name, email
        except sqlite3.Error as e:
            print(f"An error occurred while retrieving customers: {e}")
            return []
        finally:
            conn.close()

    @classmethod
    def search(cls, email):
        """Search for a customer by email."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Id, Name, Email, Password FROM Users WHERE Email = ?", (email,))
            row = cursor.fetchone()
            return cls(row[0], row[1], row[2], row[3]) if row else None  # user_id, name, email, password
        except sqlite3.Error as e:
            print(f"An error occurred while searching for the customer: {e}")
            return None
        finally:
            conn.close()

    @classmethod
    def update(cls, user_id, name=None, email=None, password=None):
        """Update customer details."""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            if name:
                cursor.execute("UPDATE Users SET Name = ? WHERE Id = ?", (name, user_id))
            if email:
                cursor.execute("UPDATE Users SET Email = ? WHERE Id = ?", (email, user_id))
            if password:
                cursor.execute("UPDATE Users SET Password = ? WHERE Id = ?", (password, user_id))
            conn.commit()
            print("Customer updated successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred while updating the customer: {e}")
        finally:
            conn.close()

    def __repr__(self):
        """Return a string representation of the customer."""
        return f"Customer(Id={self.user_id}, Name='{self.name}', Email='{self.email}')"