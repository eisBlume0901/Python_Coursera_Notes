import mysql.connector as mysql
import pandas as pd

connection = mysql.connect(host="localhost",
                           port=3306,
                           username="root",
                           password="",
                           database="classicmodels")


pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

def execute_query(script): # improved version of execute_query method which solves OperationalError and DatabaseError
    # Since i created a cursor object outside of this method wherein everytime i call the python file, it keeps creating new cursor object leading
    # to commands out of sync
    if connection.is_connected() == False:
        connection.reconnect(attempts=3, delay=5)
    Cursor = connection.cursor()
    Cursor.execute(script)
    result = Cursor.fetchall()
    Cursor.close()
    return result

# Benefits of using stored procedures vs not
# Reduce network traffic since it resides only on the database server, then executes multiple SQL statements locally
# Batching allows for the execution of multiple SQL statements in a single call which reduces the round-trip communications between the application and the database
# Centralize business logic in the database by reusing same logic in multiple applications and contributing into more consistent database
# Make the database more secure by allowing access to a particular stored procedures without providing any privileges to the underlying tables

# Limitations
# Do not rely on stored procedures for entire business logic or else complication will result to troubleshooting and maintenances

script = """CREATE PROCEDURE IF NOT EXISTS GetCustomerDetails()
            BEGIN
                SELECT
                        customerName,
                        city,
                        state,
                        postalCode,
                        country
                FROM
                        customers
                ORDER BY customerName;
            END """
execute_query(script)

script = """CALL GetCustomerDetails()""" # To find the procedure go to the database and under the tables, you can see the routines (where it stored all of the procedures created)
print(pd.DataFrame(execute_query(script), columns=["Customer Name", "City", "State", "Postal Code", "Country"]))

# IN = USER INPUT
script = """CREATE PROCEDURE IF NOT EXISTS GetOfficeByCountry(
                IN countryName VARCHAR(255)
            )
            BEGIN
                SELECT *
                FROM offices
            WHERE UPPER(country) LIKE CONCAT('%', UPPER(countryName), '%');
            END"""
execute_query(script) # Unfortunately we cannot use this format "SELECT * FROM offices WHERE UPPER(country) LIKE UPPER('%USA%')"

script = """CALL GetOfficeByCountry('USA')"""
print(pd.DataFrame(execute_query(script)))

# OUT = RESULT OF THE FUNCTION / PROCEDURE
script = """CREATE PROCEDURE IF NOT EXISTS GetOrderCountByStatus(
                IN orderStatus VARCHAR(25),
                OUT total INT
            )
            BEGIN
                SELECT COUNT(orderNumber) INTO total 
                FROM orders
                WHERE LOWER(status) LIKE CONCAT('%', LOWER(status), '%');
            END"""
execute_query(script)

script = """CALL GetOrderCountByStatus('In Process', @total)"""
execute_query(script)

script = """SELECT @total as total_in_process"""
print(execute_query(script)) # There are 326 in process order status

# INOUT - allows you to both send and retrieve values at the same time
script = """CREATE PROCEDURE IF NOT EXISTS SetCounter(
                INOUT counter INT,
                IN inc INT
            )
            BEGIN
                SET counter = counter + inc;
            END"""
execute_query(script)

script = """SET @counter = 1"""
execute_query(script)

script = """CALL SetCounter(@counter, 1)""" # 2
execute_query(script)

script = """CALL SetCounter(@counter, 1)""" # 3
execute_query(script)

script = """CALL SetCounter(@counter, 5)""" # 8
execute_query(script)

script = "SELECT @counter"
print(execute_query(script)) # 8

# DROP Keyword - to remove a stored procedure
script = """DROP PROCEDURE IF EXISTS SetCounter"""
execute_query(script)

script = """SHOW WARNINGS"""
print(execute_query(script)) #[('Note', 1304, 'PROCEDURE SetCounter already exists')], if it's not removed. If it is removed then, no message

# Declare is used to initialize a variable
# Select totalOrder is like print(totalOrder)
# This code returns the total number of orders from orders table
script = """CREATE PROCEDURE IF NOT EXISTS GetTotalOrder()
            BEGIN
                DECLARE totalOrder INT DEFAULT 0;
                
                SELECT COUNT(*) INTO totalOrder 
                    FROM orders;
                    
                SELECT totalOrder;
                
            END"""

execute_query(script)

script = """CALL GetTotalOrder()"""
print(execute_query(script)) # expected to be 326 total of orders


script = """CREATE PROCEDURE IF NOT EXISTS GetCustomerLevel(
                IN pCustomerNumber INT)
            BEGIN
                DECLARE credit DECIMAL DEFAULT 0;
                DECLARE pCustomerLevel VARCHAR(8);
                
                SELECT creditLimit
                INTO credit
                FROM customers
                WHERE customerNumber = pCustomerNumber;
                
                IF credit > 5000 THEN
                    SET pCustomerLevel = 'PLATINUM';
                ELSEIF credit <= 5000 AND credit >= 10000 THEN
                    SET pCustomerLevel = 'GOLD';
                ELSE
                    SET pCustomerLevel = 'SILVER';
                END IF;
                
                SELECT pCustomerLevel;

            END"""

execute_query(script)

script = "CALL GetCustomerLevel(447)"
print(execute_query(script))


# If-else-elseif / If-else / If-then vs Case statement
# Case statements - flexible and versatile as it allows multiple conditions and return different results based on those conditions
# If statements - useful when you are evaluating something to a TRUE/FALSE condition

script = """CREATE PROCEDURE GetDeliveryStatus(IN pOrderNumber INT)
            BEGIN
                Declare waitingDay INT DEFAULT 0;
                Declare pDeliveryStatus VARCHAR(30);
                
                SELECT DATEDIFF(shippedDate, requiredDate) INTO waitingDay
                FROM orders
                WHERE orderNumber = pOrderNumber;
                
                CASE
                    WHEN waitingDay < 0 THEN
                        SET pDeliveryStatus = 'Early Delivery';
                    WHEN waitingDay >= 1 AND waitingDay < 5 THEN
                        SET pDeliveryStatus = 'On Time';
                    WHEN waitingDay >= 5 THEN
                        SET pDeliveryStatus = 'Very Late';
                    ELSE
                        SET pDeliveryStatus = 'No Information';
                END CASE;
                
                SELECT pDeliveryStatus;
            END"""
execute_query(script)

script = """CALL GetDeliveryStatus(10100)"""
print(execute_query(script)) # Early Delivery