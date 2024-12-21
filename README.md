# E-Commerce Management System

#### A simple backend application to manage customers, products, and shopping carts for an e-commerce store.

#### By **Emmanuel Okoth**

## Description

This backend system is built using **Python** and **SQLite** to manage customers, products, and shopping carts. Users can add, delete, view, search, and update customer information, product details, and cart items. This system simulates common e-commerce management operations.

## Features

- **Add Customer**: Add new customers with their name, email, and password.
- **Delete Customer**: Delete a customer by their user ID.
- **View All Customers**: View all customers in the database.
- **Search Customer**: Search for a customer by their email.
- **Update Customer**: Update a customer's details (name, email, password).
- **Add Product**: Add products with a name, price, and quantity.
- **Delete Product**: Delete a product by its ID.
- **View All Products**: View all products available in the database.
- **Search Product**: Search for a product by its name.
- **Update Product**: Update product details (name, price, quantity).
- **Add to Cart**: Add products to a customer's shopping cart.
- **Delete from Cart**: Remove products from the shopping cart.
- **View All Carts**: View all cart items.
- **Update Cart**: Update the quantity of items in the cart.

## How to Use

### Requirements

- Python 3.x
- SQLite (or a similar database for extended functionality)
- Basic understanding of Python and SQL

### Running the Application

To run the application locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/Manu88x/Project-Python-sql
    ```

    Or download a ZIP file of the code.

2. Navigate to the project directory:

    ```bash
    cd PROJECT-E
    ```

3. Install the required dependencies:

    ```bash
    pipenv install
    ```

4. Set up the virtual environment:

    ```bash
    pipenv shell
    ```

5. Run the app:

    ```bash
    python app.py
    ```

### Accessing the Database

To view and interact with the database, navigate to the `db` folder. Right-click on the `shop.db` file and open it with an SQLite viewer.

**To install SQLite Viewer in VSCode:**

1. Go to the **Extensions** tab (the fifth icon on the left side of your screen).
2. Search for **SQLite Viewer** and install it.

## Main Menu Options:

Once the application is set up and running, you will be presented with the Main Menu. Below are the available options and their descriptions(remember use numbers as options):

### **Option 1: Add (Customer/Product/Cart)**
- **Purpose:** Add new entities (customers, products, or cart items) to the database.
- **How to Use:**
  - Select option `1` from the Main Menu.
  - Choose one of the following actions:
    - **Add a Customer:** Enter customer details such as name, email, and password.
    - **Add a Product:** Enter product details such as name, price, and quantity.
    - **Add to Cart:** Enter the user ID, product ID, and quantity to add a product to the cart.

### **Option 2: Delete (Customer/Product/Cart)**
- **Purpose:** Delete a customer, product, or cart item from the database.
- **How to Use:**
  - Select option `2`.
  - Choose what to delete:
    - **Delete a Customer:** Enter the unique user ID of the customer.
    - **Delete a Product:** Enter the unique product ID.
    - **Delete a Cart Item:** Enter the unique cart item ID.

### **Option 3: View All Customers**
- **Purpose:** View a list of all customers in the database.
- **How to Use:**
  - Select option `3` to display a list of all customers, including their name, email, and user ID.

### **Option 4: Search Customer**
- **Purpose:** Search for a customer by their email address.
- **How to Use:**
  - Select option `4` and input the customer’s email address.
  - If the customer exists, their details will be displayed.

### **Option 5: Update Customer**
- **Purpose:** Update the details of an existing customer.
- **How to Use:**
  - Select option `5`.
  - Enter the customer’s user ID.
  - You can update their name, email, or password. Leave any fields blank if you do not wish to update them.

### **Option 6: View All Products**
- **Purpose:** View a list of all products in the database.
- **How to Use:**
  - Select option `6` to see a list of all products, including their name, price, and quantity.

### **Option 7: Search Product**
- **Purpose:** Search for a product by its name.
- **How to Use:**
  - Select option `7` and enter the product name.
  - If the product exists, its details will be displayed.

### **Option 8: Update Product**
- **Purpose:** Update an existing product's details.
- **How to Use:**
  - Select option `8`.
  - Provide the product ID.
  - You can update the product name, price, or quantity. Leave any fields blank if no update is needed.

### **Option 9: View All Carts**
- **Purpose:** View all shopping cart items.
- **How to Use:**
  - Select option `9` to view all cart items, showing which products are in each customer’s cart.

### **Option 10: Search Cart**
- **Purpose:** Search for a cart by user ID.
- **How to Use:**
  - Select option `10` and input the user ID.
  - If no cart is found for that user, you will see a "No cart items found" message.

### **Option 11: Update Cart**
- **Purpose:** Update the quantity of items in a shopping cart.
- **How to Use:**
  - Select option `11`.
  - Provide the cart ID and the updated quantity for the items.

### **Option 12: Exit**
- **Purpose:** Exit the application.
- **How to Use:**
  - Select option `12` to exit the program.

---

## Technologies Used

- **Python**
- **SQLite**

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

- **Email**: Emmanuel.okoth@student.moringaschool.com

## License

MIT License

Copyright &copy; 2024 Emmanuel Okoth

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
