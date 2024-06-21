from database_utils import Database
import pandas as pd

db = Database()
db_connection = db.connect("learning_mysql_with_python")

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

# Accessing two different tables (wit
# Subquery
sql = "SELECT * FROM EMPLOYEES WHERE JOB_ID IN (SELECT JOB_IDENT FROM JOBS)"
employees_matching_in_jobs_table = db.execute_query(sql)
print(pd.DataFrame(employees_matching_in_jobs_table))

sql = "SELECT JOB_TITLE, MIN_SALARY, MAX_SALARY, JOB_IDENT FROM JOBS WHERE JOB_IDENT IN (SELECT JOB_ID FROM EMPLOYEES WHERE SALARY > 70000)"
job_info_for_employees_earning_over_70000 = db.execute_query(sql)
print(pd.DataFrame(job_info_for_employees_earning_over_70000, columns=["Job Title", "Minimum Salary", "Maximum Salary", "Job Identification"]))

sql = "SELECT * FROM EMPLOYEES WHERE JOB_ID IN (SELECT JOB_IDENT FROM JOBS WHERE JOB_TITLE LIKE 'Jr. Designer')"
junior_designers = db.execute_query(sql)
print(pd.DataFrame(junior_designers))

sql = "SELECT * FROM JOBS WHERE JOB_IDENT IN (SELECT JOB_ID FROM EMPLOYEES WHERE YEAR(B_DATE) > 1976)"
job_info_of_employees_1977_and_up = db.execute_query(sql)
print(pd.DataFrame(job_info_of_employees_1977_and_up))

sql = "SELECT * FROM EMPLOYEES WHERE DEP_ID = (SELECT MAX(DEPT_ID_DEP) FROM DEPARTMENTS)"
highest_department_id = db.execute_query(sql)
print(pd.DataFrame(highest_department_id))


# Implicit Join / Full Join / Cartesian Join
sql = "SELECT E.EMP_ID, E.F_NAME, E.L_NAME, J.JOB_TITLE FROM EMPLOYEES E, JOBS J WHERE E.JOB_ID = J.JOB_IDENT"
employees_matching_in_jobs_table_v2 = db.execute_query(sql)
print(pd.DataFrame(employees_matching_in_jobs_table_v2, columns=["Employee ID", "First Name", "Last Name", "Job Title"]))

sql = "SELECT * FROM EMPLOYEES E, JOBS J WHERE E.JOB_ID = J.JOB_IDENT AND J.JOB_TITLE LIKE 'Jr. Designer'"
junior_designers_v2 = db.execute_query(sql)
print(pd.DataFrame(junior_designers_v2))

sql = "SELECT J.* FROM EMPLOYEES E, JOBS J WHERE E.JOB_ID = J.JOB_IDENT AND YEAR(E.B_DATE) > 1976"
job_info_of_employees_1977_and_up_v2 = db.execute_query(sql)
print(pd.DataFrame(job_info_of_employees_1977_and_up_v2))

sql = "SELECT F_NAME, DEP_NAME FROM EMPLOYEES, DEPARTMENTS WHERE DEPT_ID_DEP = DEP_ID"
employees_with_its_department_names = db.execute_query(sql)
print(pd.DataFrame(employees_with_its_department_names))