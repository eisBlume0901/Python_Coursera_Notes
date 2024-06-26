import mysql.connector as mysql
import pandas as pd

conn = mysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="",
                     database="learning_mysql_with_python")

cur = conn.cursor()

def execute_query(script):
    cur.execute(script)
    return cur.fetchall()

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

# script = """CREATE VIEW IF NOT EXISTS EMPSALARY
#             AS SELECT EMP_ID, F_NAME, L_NAME, B_DATE, SEX, SALARY
#             FROM EMPLOYEES"""
# execute_query(script)

# script = """SELECT * FROM EMPSALARY"""
# print(pd.DataFrame(execute_query(script), columns=["EMP_ID", "F_NAME", "L_NAME", "B_DATE", "SEX", "SALARY"]))

# Review implicit joins under learning_accessing_multiple_tables_with_subqueries_and_implicit_joins.py
# script = """CREATE OR REPLACE VIEW EMPSALARY
#             AS SELECT E.EMP_ID, E.F_NAME, E.L_NAME, E.B_DATE, E.SEX, J.JOB_TITLE, J.MIN_SALARY, J.MAX_SALARY
#             FROM EMPLOYEES E, JOBS J
#             WHERE E.JOB_ID = J.JOB_IDENT"""
# execute_query(script)

# script = """SELECT * FROM EMPSALARY"""
# print(pd.DataFrame(execute_query(script), columns=["EMP_ID", "F_NAME", "L_NAME", "B_DATE", "SEX", "JOB_TITLE", "MIN_SALARY", "MAX_SALARY"]))

# script = "DROP VIEW EMPSALARY"
# print(pd.DataFrame(execute_query(script)))


# script = """CREATE VIEW IF NOT EXISTS EMP_DEPT
#             AS SELECT EMP_ID, F_NAME, L_NAME, DEP_ID
#             FROM EMPLOYEES"""
# execute_query(script)

# script = """CREATE OR REPLACE VIEW EMP_DEPT
#             AS SELECT E.EMP_ID, E.F_NAME, E.L_NAME
#             FROM EMPLOYEES E, DEPARTMENTS D
#             WHERE E.DEP_ID = D.DEPT_ID_DEP"""
# execute_query(script)

# script = """SELECT * FROM EMP_DEPT"""
# print(pd.DataFrame(execute_query(script), columns=["EMP_ID", "F_NAME", "L_NAME"]))

# script = """DROP VIEW EMP_DEPT"""
# print(pd.DataFrame(execute_query(script)))