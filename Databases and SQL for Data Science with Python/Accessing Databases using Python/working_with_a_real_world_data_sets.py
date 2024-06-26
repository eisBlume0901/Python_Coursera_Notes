import sqlite3
import pandas as pd

# Fetching table data
# SQLite3 SELECT name FROM sqlite_master WHERE type = "table"
# MySQL SHOW TABLES

# Getting table attributes
# SQLite3 PRAGMA table_info([table_name])
# MySQL DESCRIBE table_name

conn = sqlite3.connect("chicago_datas.db")
cur = conn.cursor()

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

# multi means to insert all rows of the dataframe instead of doing one row at a time
# chicago_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv")
# chicago_df.to_sql("CENSUS_DATA", conn, if_exists="replace", index=False, method="multi")
#
# chicago_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv")
# chicago_df.to_sql("CHICAGO_CRIME_DATA", conn, if_exists="replace", index=False, method="multi")
#
# chicago_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv")
# chicago_df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", conn, if_exists="replace", index=False, method="multi")

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type = 'table'", conn)
print(tables)

chicago_public_school_columns = pd.read_sql_query("PRAGMA table_info(CHICAGO_PUBLIC_SCHOOLS_DATA)", conn)
print(chicago_public_school_columns)

chicago_public_school_num_columns = pd.read_sql_query("SELECT COUNT(name) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA')", conn)
print(chicago_public_school_num_columns)

chicago_public_school_columns_datatype_length = pd.read_sql_query("SELECT name, type, length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC SCHOOLS_DATA')", conn)
print(chicago_public_school_columns_datatype_length)

# Question 1 Is the column name for the "SCHOOL ID" attribute in upper or mixed case? Mixed Case
chicago_public_school_school_id_attribute = pd.read_sql_query("SELECT name FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA') WHERE UPPER(name) = 'SCHOOL_ID' ", conn)
print(chicago_public_school_school_id_attribute)

# Question 2  What is the name of "Community Area Name" column in your table? Does it have spaces? COMMUNITY_AREA_NAME
chicago_public_school_community_area_name = pd.read_sql_query("SELECT name FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA') WHERE UPPER(name) LIKE '%COMMUNITY%AREA%NAME%'", conn)
print(chicago_public_school_community_area_name)

# Question 3 Are there any columns in whose names the spaces and paranthesis (round brackets) have been replaced by the underscore character "\_ YES
chicago_public_school_check_underscores = pd.read_sql_query("SELECT name FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA') WHERE name LIKE '%_%'", conn)
print(chicago_public_school_check_underscores)

# Problem 1 How many Elementary Schools are in the dataset? NOTE: the CHICAGO_PUBLIC_SCHOOLS_DATA is not working but the SQL query is correct
chicago_public_school_elementary = pd.read_sql_query("SELECT COUNT('Elementary, Middle, or High School') FROM CHICAGO_PUBLIC_SCHOOLS_DATA where 'Elementary, Middle, or High School' LIKE 'ES'", conn)
print(chicago_public_school_elementary)

# Problem 2 What is the highest Safety Score?
chicago_public_school_elementary_highest_safety_score = pd.read_sql_query("SELECT MAX(SAFETY_SCORE) AS HIGHEST_SAFETY_SCORE FROM CHICAGO_PUBLIC_SCHOOLS_DATA", conn)
print(chicago_public_school_elementary_highest_safety_score)

# Problem 3 Which schools have highest Safety Score?
chicago_public_schools_data_with_highest_safety_score = pd.read_sql_query("SELECT NAME_OF_SCHOOL FROM CHICAGO_PUBLIC_SCHOOLS_DATA WHERE SAFETY_SCORE IN (SELECT MAX(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS_DATA)", conn)
print(chicago_public_schools_data_with_highest_safety_score)

# Problem 4 What are the top 10 schools with the highest "Average Student Attendance"?¶
chicago_public_schools_data_top_10_schools_average_student_attendance = pd.read_sql_query("SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE FROM CHICAGO_PUBLIC_SCHOOLS_DATA ORDER BY AVERAGE_STUDENT_ATTENDANCE DESC LIMIT 10", conn)
print(chicago_public_schools_data_top_10_schools_average_student_attendance)

# Problem 5 Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance
chicago_public_schools_data_top_5_schools_with_lowest_average_student_attendance = pd.read_sql_query("SELECT NAME_OF_SCHOOL, AVERAGE_STUDENT_ATTENDANCE FROM CHICAGO_PUBLIC_SCHOOLS_DATA ORDER BY AVERAGE_STUDENT_ATTENDANCE ASC LIMIT 5", conn)
print(chicago_public_schools_data_top_5_schools_with_lowest_average_student_attendance)

# Problem 6 Now remove the '%' sign from the above result set for Average Student Attendance column
chicago_public_schools_data_replace = pd.read_sql_query("SELECT REPLACE(AVERAGE_STUDENT_ATTENDANCE, '%', '') FROM CHICAGO_PUBLIC_SCHOOLS_DATA", conn)
print(chicago_public_schools_data_replace)