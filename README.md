INTRODUCTION PROJECT : 
  This project aims to develop a simple cashier system that utilizes SQLAlchemy as an Object-Relational Mapping (ORM) and utilizes a SQLite database for data storage. The system can be used in various types of businesses, such as small shops, supermarkets, or restaurants.

The key features of this cashier system include:

Add Item: Users can add new items to the database. Each item will have information such as name, price, and available stock quantity. The item data will be stored in a separate table in the SQLite database.

Delete Item: Users can remove items that are no longer needed from the database. This action will update the data and remove the corresponding item entry from the table.

Reset Item: This feature allows users to reset the stock quantity of a particular item to its initial value. For example, if there is a change in stock or replacement of a product, users can reset the stock quantity to a new value.

Check Order: Users can view the list of items that have been added to the shopping cart or order. The system will retrieve data from the item table in the database and display information such as name, price, and stock quantity.

Check Out: When users finish shopping, this feature enables them to complete the transaction by calculating the total payment based on the items in the shopping cart. The system will deduct the purchased item quantity from the database.

Database Management: The system utilizes SQLAlchemy as an ORM for interacting with the SQLite database. This allows users to perform CRUD (Create, Read, Update, Delete) operations on the item table, such as adding, deleting, modifying, or updating item data.

The goal of this project is to provide a simple yet effective cashier solution by leveraging SQLAlchemy and a SQLite database. With features such as Add Item, Delete Item, Reset Item, Check Order, and Check Out, this system can assist users in managing inventory, conducting sales transactions, and monitoring stock efficiently.


SETEP PROJECT :
SQL SQLAlchemy
![alt text](https://github.com/Badra24/cashirPY/blob/main/picture/sqlkAlchemy.png?raw=true)
1. Import the necessary modules: `sqlalchemy.create_engine`, `sqlalchemy.Table`, `sqlalchemy.MetaData`, `sqlalchemy.Integer`, `sqlalchemy.String`, `sqlalchemy.Float`, `sqlalchemy.Column`, `sqlalchemy.orm.sessionmaker`.

2. Create a database engine using the `create_engine()` function, specifying the connection URL for the SQLite database file.

3. Create a `MetaData` object that holds all the database schema information.

4. Define the table using the `Table()` function, specifying the table name, metadata, and column definitions.

5. Create the table in the database by calling the `create_all()` method on the metadata object and passing in the engine.

6. Set up a session by creating a session factory using the `sessionmaker()` function and binding it to the engine.

7. Create a session object by calling the session factory.

These steps will establish a connection to the SQLite database, define the table structure, create the table in the database, and set up a session for performing database operations.

ADD ITEM, DELETE ITEM, RESET TRANSANCTION,CEHCK ORDER
![alt text](https://github.com/Badra24/cashirPY/blob/main/picture/sintax%201.png?raw=true)
Based on the provided code, here is a description of the functions:

1. `add_item(name, qty, price)`: This function adds an item to the existing list of items. It takes parameters for the name, quantity (qty), and price of the item. The function calculates the total price by multiplying the quantity and price and then appends the item dictionary to the `items` list.

2. `delete_item(name)`: This function deletes an item from the `items` list based on the provided item name. It iterates over the `items` list and creates a new list comprehension, excluding the item with a matching name (case-insensitive comparison). The resulting list is assigned back to the `items` list.

3. `reset_transaction()`: This function resets the `items` list by assigning an empty list to the global variable `items`. It clears the transaction data, essentially starting a new transaction.

4. `check_order()`: This function checks the validity of the order. It iterates over each item in the `items` list and checks if the name, quantity, and price fields are not empty. If any of the fields are empty, it returns the string "Terdapat kesalahan input data" (There is an input data error). If all the fields are filled correctly for all items, it returns the string "Pemesanan sudah benar" (The order is correct).

These functions provide basic functionality for managing a list of items, adding new items, deleting items, resetting the transaction, and checking the validity of the order.

CHECK OUT :
![alt text](https://github.com/Badra24/cashirPY/blob/main/picture/sintax%202.png?raw=true)
Based on the provided code snippet, here is a description of the `check_out()` function:

The `check_out()` 

1. Create a dictionary, `items_bought`, using a dictionary comprehension to map each item's name to a list containing its quantity and price. This dictionary represents the items that have been bought during the transaction.

2. Print the message "Item yang dibeli adalah: " followed by the `items_bought` dictionary. This displays the items that have been purchased.

3. Calculate the total payment by summing up the "total" value for each item in the `items` list.

4. Determine the discount percentage based on the total payment. If the total payment is greater than 500,000, the discount percentage is 7%. If the total payment is greater than 300,000, the discount percentage is 6%. If the total payment is greater than 200,000, the discount percentage is 5%. Otherwise, there is no discount (0% discount).

5. Calculate the total payment after applying the discount by subtracting the discount amount from the total payment.

6. Call the `insert_to_table()` function to insert the transaction details, such as the total payment after the discount and the discount percentage, into a table (not shown in the provided code).

7. Return the total payment after the discount (`total_after_disc`) and the discount percentage (`disc`).

This function calculates the total payment for the purchased items, applies any applicable discount based on the total payment amount, and returns the final total payment after the discount and the discount percentage.

INSER TABEL :
![alt text](https://github.com/Badra24/cashirPY/blob/main/picture/inserttabel.png?raw=true)
The `insert_to_table()` :

1. Inside a try-except block, iterate over each item in the `items` list.

2. Construct an insert statement using the `transaksi.insert().values()` method. The values to be inserted include the following:

   - `no_id=1`: Assigns a constant value of 1 to the `no_id` column.
   - `nama_item=item["name"]`: Inserts the name of the item into the `nama_item` column.
   - `jumlah_item=item["qty"]`: Inserts the quantity of the item into the `jumlah_item` column.
   - `harga=item["price"]`: Inserts the price of the item into the `harga` column.
   - `total_harga=item["total"]`: Inserts the total price of the item into the `total_harga` column.
   - `diskon=disc`: Inserts the discount percentage (`disc`) into the `diskon` column.
   - `harga_diskon=total_after_disc`: Inserts the total payment after discount (`total_after_disc`) into the `harga_diskon` column.

3. Execute the insert statement by calling `session.execute(ins)`.

4. Commit the changes to the database by calling `session.commit()`.

5. If any exception occurs during the insertion process, the code will catch the exception and print an error message displaying the specific error.

This function inserts the transaction details, including item name, quantity, price, total price, discount percentage, and total payment after discount, into a table named `transaksi` using SQLAlchemy's `execute()` method and commits the changes to the database.

RESULT AND TESTCASE:
![alt text](https://github.com/Badra24/cashirPY/blob/main/picture/tasecase.png?raw=true)

1. Test Case 1:
   - Action: Adding items 'Ayam Goreng' with a quantity of 2 and a price of 20,000, and 'Pasta Gigi' with a quantity of 3 and a price of 15,000.
   - Result: The items are added to the `items` list. Printing the `items` list will show:
     ```
     [{'name': 'Ayam Goreng', 'qty': 2, 'price': 20000, 'total': 40000},
      {'name': 'Pasta Gigi', 'qty': 3, 'price': 15000, 'total': 45000}]
     ```

2. Test Case 2:
   - Action: Deleting the item 'Pasta Gigi'.
   - Result: The item 'Pasta Gigi' is removed from the `items` list. Printing the `items` list will show:
     ```
     [{'name': 'Ayam Goreng', 'qty': 2, 'price': 20000, 'total': 40000}]
     ```

3. Test Case 3:
   - Action: Resetting the transaction.
   - Result: The `items` list is emptied. Printing the `items` list will show an empty list: `[]`.

4. Test Case 4:
   - Action: Adding items 'Ayam Goreng' with a quantity of 2 and a price of 20,000, 'Pasta Gigi' with a quantity of 3 and a price of 15,000, 'Mainan Mobil' with a quantity of 1 and a price of 200,000, and 'Mie Instan' with a quantity of 5 and a price of 3,000.
   - Result: The items are added to the `items` list. Printing the `items` list will show:
     ```
     [{'name': 'Ayam Goreng', 'qty': 2, 'price': 20000, 'total': 40000},
      {'name': 'Pasta Gigi', 'qty': 3, 'price': 15000, 'total': 45000},
      {'name': 'Mainan Mobil', 'qty': 1, 'price': 200000, 'total': 200000},
      {'name': 'Mie Instan', 'qty': 5, 'price': 3000, 'total': 15000}]
     ```

5. Test Case 5:
   - Action: Performing the checkout process and obtaining the total payment (`total`) and discount percentage (`disc`).
   - Result: The total payment (`total`) after applying the discount and the discount percentage (`disc`) are calculated based on the total price of all items. The values may vary depending on the total price. The result will be printed as "Total belanja yang harus dibayarkan adalah: [total]".
     Example output: "Total belanja yang harus dibayarkan adalah: 260000".

These test cases demonstrate the functionality of adding items, deleting items, resetting the transaction, and performing the checkout process to calculate the total payment and discount percentage.
PICTURE OF OUTPUT TERMINAL RESULT :
![alt text](https://github.com/Badra24/cashirPY/blob/main/picture/testecas3.png?raw=true)


