from database_utils import Database
import pandas as pd

db = Database()
db_connection = db.connect("learning_mysql_with_python")

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

# Subquery in where clause
sql = "SELECT * FROM EMPLOYEES WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES)"
comparing_salary_from_average_salary = db.execute_query(sql)
print(comparing_salary_from_average_salary)
print(pd.DataFrame(comparing_salary_from_average_salary))

sql = "SELECT F_NAME, L_NAME FROM EMPLOYEES WHERE B_DATE = (SELECT MIN(B_DATE) FROM EMPLOYEES)"
oldest_employee = db.execute_query(sql)
print(oldest_employee)
print(pd.DataFrame(oldest_employee))

# YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, B_DATE)))
sql = "SELECT * FROM EMPLOYEES WHERE YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, B_DATE))) > (SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, B_DATE)))) FROM EMPLOYEES)"
employees_older_than_average_age_of_all_employees = db.execute_query(sql)
print(employees_older_than_average_age_of_all_employees)
print(pd.DataFrame(employees_older_than_average_age_of_all_employees))


# Subquery in select clause (column expressions)
sql = "SELECT EMP_ID, SALARY, (SELECT MAX(SALARY) FROM EMPLOYEES) AS MAX_SALARY FROM EMPLOYEES"
comparing_salary_from_maximum_salary = db.execute_query(sql)
print(comparing_salary_from_maximum_salary)
print(pd.DataFrame(comparing_salary_from_maximum_salary))

# Subquery in from clause (derived tables or table expressions)
sql = "SELECT AVG(SALARY) FROM (SELECT SALARY FROM EMPLOYEES ORDER BY SALARY DESC LIMIT 5) AS SALARY_TABLE"
average_salary_from_top_5_earners_in_company = db.execute_query(sql)
print(average_salary_from_top_5_earners_in_company)
print(pd.DataFrame(average_salary_from_top_5_earners_in_company))

sql = "SELECT AVG(SALARY) FROM (SELECT SALARY FROM EMPLOYEES ORDER BY SALARY LIMIT 5) AS SALARY_TABLE"
average_salary_from_top_5_least_earners_in_company = db.execute_query(sql)
print(average_salary_from_top_5_least_earners_in_company)
print(pd.DataFrame(average_salary_from_top_5_least_earners_in_company))

sql = "SELECT EMPL_ID, YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE))), (SELECT AVG(YEAR(FROM_DAYS(DATEDIFF(CURRENT_DATE, START_DATE)))) FROM JOB_HISTORY) FROM JOB_HISTORY"
years_of_service_of_each_employee = db.execute_query(sql)
print(years_of_service_of_each_employee)
print(pd.DataFrame(years_of_service_of_each_employee))

db.close()