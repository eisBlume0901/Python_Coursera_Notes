import mysql.connector as mysql
import pandas as pd

connection = mysql.connect(host="localhost",
                           port=3306,
                           username="root",
                           password="",
                           database="learning_mysql_with_python")

def execute_query(script):
    if connection.is_connected() == False:
        connection.reconnect(attempts=3, delay=5)
    Cursor = connection.cursor()
    Cursor.execute(script)
    result = Cursor.fetchall()
    Cursor.close()
    return result

# Inner join
sql_script = """SELECT E.F_NAME, E.L_NAME, JH.START_DATE FROM EMPLOYEES E INNER JOIN JOB_HISTORY JH ON E.EMP_ID = JH.EMPL_ID WHERE E.DEP_ID = 5"""
print(pd.DataFrame(execute_query(sql_script)))

# Left outer join, left table is EMPLOYEES
sql_script = """SELECT E.F_NAME, E.L_NAME, JH.START_DATE FROM EMPLOYEES E LEFT OUTER JOIN JOB_HISTORY JH ON E.EMP_ID = JH.EMPL_ID"""
print(pd.DataFrame(execute_query(sql_script)))

# Right outer join, right table is JOB_HISTORY
sql_script = """SELECT E.F_NAME, E.L_NAME, JH.START_DATE FROM EMPLOYEES E RIGHT OUTER JOIN JOB_HISTORY JH ON E.EMP_ID = JH.EMPL_ID"""
print(pd.DataFrame(execute_query(sql_script)))

# Full outer join (There is no OUTER JOIN keyword in MYSQL; Thus, we have to use UNION)
sql_script = """SELECT E.F_NAME, E.L_NAME, D.DEP_NAME FROM EMPLOYEES E LEFT OUTER JOIN DEPARTMENTS D ON E.DEP_ID = D.DEPT_ID_DEP
UNION SELECT E.F_NAME, E.L_NAME, D.DEP_NAME FROM EMPLOYEES E RIGHT OUTER JOIN DEPARTMENTS D ON E.DEP_ID = D.DEPT_ID_DEP"""
print(pd.DataFrame(execute_query(sql_script)))


# Practice
# Question: Retrieve the names, job start dates, and job titles of all employees who work for department number 5.
sql_script = """SELECT E.F_NAME, E.L_NAME, JH.START_DATE, J.JOB_TITLE FROM EMPLOYEES E INNER JOIN JOB_HISTORY JH ON E.EMP_ID = JH.EMPL_ID INNER JOIN JOBS J ON E.JOB_ID = J.JOB_IDENT WHERE E.DEP_ID = 5"""
print(pd.DataFrame(execute_query(sql_script)))

# Question: Retrieve employee ID, last name, and department ID for all employees (left join) but department names for only those born before 1980.
sql_script = """SELECT E.EMP_ID, E.L_NAME, D.DEP_NAME FROM EMPLOYEES E LEFT OUTER JOIN DEPARTMENTS D ON E.DEP_ID = D.DEPT_ID_DEP WHERE YEAR(E.B_DATE) < 1980"""
print(pd.DataFrame(execute_query(sql_script)))

# Question: Retrieve the first name and last name of all employees but department ID and department names only for male employees (full outer join)
sql_script = """SELECT E.F_NAME, E.L_NAME, D.DEPT_ID_DEP, D.DEP_NAME FROM EMPLOYEES E LEFT OUTER JOIN DEPARTMENTS D ON E.DEP_ID = D.DEPT_ID_DEP WHERE E.SEX = 'M' 
UNION SELECT E.F_NAME, E.L_NAME, D.DEPT_ID_DEP, D.DEP_NAME FROM EMPLOYEES E RIGHT OUTER JOIN DEPARTMENTS D ON E.DEP_ID = D.DEPT_ID_DEP WHERE E.SEX = 'M'"""
print(pd.DataFrame(execute_query(sql_script)))