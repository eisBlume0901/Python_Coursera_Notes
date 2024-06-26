import sqlite3 as sql
import pandas
import pandas as pd

def create_sqlite_database(filename):
    conn = None
    try:
        conn = sql.connect(filename)
        print(sql.sqlite_version)
    except sql.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def execute_query(sql_script):
    cursor = None
    try:
        with sql.connect("learning_sqlite3_with_python.db") as conn:
            cursor = conn.cursor()
            cursor.execute(sql_script)
            conn.commit()
    except sql.Error as e:
        print(e)
    return cursor.fetchall() # use fetchmany(numberOfDatasToRetrieve)

if __name__ == '__main__': # public static void main(String[] args) counterpart
    sql_script = """CREATE TABLE IF NOT EXISTS instructors (
                id INTEGER PRIMARY KEY, 
                first_name VARCHAR(20),
                last_name VARCHAR(20),
                city VARCHAR(20),
                country_code CHAR(2));
        """

    create_sqlite_database("learning_sqlite3_with_python.db")
    create_table = execute_query(sql_script)

    sql_script = """INSERT INTO instructors VALUES (1, 'Mary Claire', 'Ethereal', 'Wales', 'UK');"""
    first_data = execute_query(sql_script)

    sql_script = """INSERT INTO instructors VALUES 
                    (2, 'Amelia', 'Watson', 'Britain', 'UK'), 
                    (3, 'Emerald', 'Greenleaf', 'Birmingham', 'UK');"""
    insert_two_datas = execute_query(sql_script)

    sql_script = """SELECT * FROM instructors"""
    fetch_instructor_datas = execute_query(sql_script)
    for row in fetch_instructor_datas:
        print(row)

    conn = sql.connect("learning_sqlite3_with_python.db")
    instructor_df = pd.read_sql_query("select * from instructors", conn)
    print(instructor_df)
    print(instructor_df.shape)
    print(instructor_df[["first_name"]])
    conn.close()
