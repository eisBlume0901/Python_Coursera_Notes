
import mysql.connector as mysql

# Establish database connection
connection = mysql.connect(host="localhost",
                           port=3306,
                           username="root",
                           password="",
                           database="learning_acid_transactions")

def execute_query(script):
    if connection.is_connected() == False:
        connection.reconnect(attempts=3, delay=5)
    Cursor = connection.cursor()
    Cursor.execute(script)
    result = Cursor.fetchall()
    Cursor.close()
    return result

# Complicated logic is not suitable for stored procedures (no debuggers and testers) because it will affect all data rows
# Better to not do mass update too or just use simple SQL statements instead

script = """CREATE PROCEDURE IF NOT EXISTS BUY_SHOES(
            IN accountNumber VARCHAR(4),
            IN accountName VARCHAR(15),
            IN productName VARCHAR(30),
            IN numOrders INT)
            BEGIN
                DECLARE acctBalance DECIMAL(8,2);
                DECLARE productPrice DECIMAL(8, 2);
                DECLARE productStock INT;
                DECLARE productValue DECIMAL(8, 2);

                START TRANSACTION;

                SELECT Balance INTO acctBalance FROM bankaccounts WHERE AccountNumber = accountNumber AND AccountName = accountName LIMIT 1;
                SELECT Price, Stock INTO productPrice, productStock FROM shoeshop WHERE LOWER(Product) LIKE LOWER(productName) LIMIT 1;

                SET productValue = productPrice * numOrders;
                
                IF acctBalance >= productPrice * numOrders AND productStock >= numOrders THEN
                    UPDATE bankaccounts
                    SET Balance = Balance + productValue
                    WHERE AccountNumber = 'B003';

                    UPDATE bankaccounts
                    SET Balance = Balance - productValue
                    WHERE AccountNumber = accountNumber AND AccountName = accountName;

                    UPDATE shoeshop
                    SET Stock = Stock - numOrders
                    WHERE LOWER(Product) = LOWER(productName);

                    COMMIT;
                ELSE
                    ROLLBACK;
                END IF;
            END;
        """
execute_query(script)

script = """CALL BUY_SHOES('B002', 'James', 'Boots', 2)"""
execute_query(script)

script = """SELECT * FROM bankaccounts WHERE AccountName = 'Shoe Shop';"""
print(execute_query(script))

# script = """CALL BUY_SHOES('B002', 'James', 'Trainers', 4)"""
# execute_query(script)
#
# script = """SELECT * FROM bankaccounts WHERE AccountName = 'Shoe Shop';"""
# print(execute_query(script))
#
# script = """CALL BUY_SHOES('B002', 'James', 'Brogues', 1)"""
# execute_query(script)
#
# script = """SELECT * FROM bankaccounts WHERE AccountName = 'Shoe Shop';"""
# print(execute_query(script))