import mysql.connector

# DB Connection details
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Travisasutsa01.", database="company"
)

mycursor = mydb.cursor()

# create a table named 'customers' (if it doesn't exist)
mycursor.execute(
    """
                 CREATE TABLE IF NOT EXISTS customers(
                     id INT AUTO_INCREMENT PRIMARY KEY,
                     name VARCHAR(255) NOT NULL,
                     email VARCHAR(255) NOT NULL UNIQUE)
                     """
)
print("Table created successfully!")

# insert some customer data
sql = "INSERT IGNORE INTO customers (name, email) VALUES (%s, %s)"
val = ("Geoffrey Mutai", "mutai@gmail.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted to DB")

val = ("User Name", "username@gmail.com")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted")

# read all customer data
mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()

print("customers : ")
for row in result:
    print(row)

# Update a customer's data e.g email
sql = "UPDATE customers SET email = %s WHERE id = %s"
val = ("updatedemail@gmail.com", 2)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) updated")

# Read the updated customer data

mycursor.execute("SELECT * FROM customers WHERE id = 2")
myresult = mycursor.fetchone()
print("Updated Customer: ", myresult)


# Delete a customer
sql = "DELETE FROM customers WHERE id = 1"
mycursor.execute(sql)
mydb.commit()

print("Remaining  users:", result)

mycursor.close()
mydb.close()

print("DB Connection closed")
