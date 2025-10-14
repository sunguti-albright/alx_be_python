"""
Challenge: Library Management System Imagine you’re building a simple library management system using Python and a MySQL database. This system will allow you to store information about books (title, author, ISBN) and perform basic operations like adding new books, searching by title, and listing all books in the library.

Tasks: * Setting Up: * Install the mysql-connector-python library using pip install mysql-connector-python. * Create a MySQL database and a table named books with columns for id (INT, Auto-Increment primary key), title (VARCHAR(255)), author (VARCHAR(255)), and ISBN (VARCHAR(255)).

Connect to Database:

Write Python code to connect to your MySQL database using the provided connection details (replace placeholders with your actual credentials).
Adding Books:
Implement a function that takes book details (title, author, ISBN) as input and inserts a new record into the books table using an INSERT query.
Searching Books:

Write a function that allows users to search for books by title. It should use a SELECT query with a WHERE clause to filter results based on the user’s input. Print the details of any matching books.
Listing All Books:

Create a function that retrieves all book information from the books table using a SELECT query. Print the details of all books in a user-friendly format.
(Bonus Challenge:

Implement functionality to delete a book from the library by its ID. Use a DELETE query with a WHERE clause to remove the specified book.

Remember: Make sure to commit any changes to the database using mydb.commit(). Close the connection to the database using mycursor.close() and mydb.close() when you’re finished.
"""
import mysql.connector
