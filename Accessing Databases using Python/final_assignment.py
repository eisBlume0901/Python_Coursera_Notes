import mysql.connector as mysql
import pandas as pd
import requests
import os

conn = mysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="",
                     database="learning_mysql_with_python")


pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

census_data_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv"
crime_data_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv"
public_schools_data_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv"
def convert_link_to_downloadable_csv_file(url, file_name):
    response = requests.get(url)
    path = os.path.join(os.getcwd(), file_name)

    with open(path, "wb") as file:
        file.write(response.content)

convert_link_to_downloadable_csv_file(census_data_url, "census_data.csv")
convert_link_to_downloadable_csv_file(crime_data_url, "crime_data.csv")
convert_link_to_downloadable_csv_file(public_schools_data_url, "chicago_public_schools.csv")

def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Problem 1 Find the total number of crimes recorded in the CRIME table
script = "SELECT COUNT(DISTINCT(CASE_NUMBER)) FROM CHICAGO_CRIME_DATA"
print(execute_query(script)) #

# Problem 2 List community area names and numbers with per capita income less than 11000
script = "DESCRIBE CENSUS_DATA"
print(pd.DataFrame(execute_query(script)))

script = "SELECT COMMUNITY_AREA_NAME, COMMUNITY_AREA_NUMBER FROM CENSUS_DATA WHERE PER_CAPITA_INCOME < 11000"
print(pd.DataFrame(execute_query(script)))

# Problem 3 List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis)
script = "DESCRIBE CHICAGO_CRIME_DATA"
print(pd.DataFrame(execute_query(script)))

script = "SELECT * FROM CHICAGO_CRIME_DATA LIMIT 5"
print(pd.DataFrame(execute_query(script)))

script = "SELECT CASE_NUMBER FROM CHICAGO_CRIME_DATA WHERE UPPER(DESCRIPTION) LIKE '%MINOR%'"
print(pd.DataFrame(execute_query(script)))

# Problem 4 List all kidnapping crimes involving a child?
script = "SELECT * FROM CHICAGO_CRIME_DATA WHERE UPPER(DESCRIPTION) LIKE '%CHILD%' AND UPPER(PRIMARY_TYPE) LIKE '%KIDNAPPING%'"
print(pd.DataFrame(execute_query(script)))

# Problem 5 List the kind of crimes that were recorded at schools
script = "SELECT DISTINCT(PRIMARY_TYPE) FROM CHICAGO_CRIME_DATA WHERE UPPER(LOCATION_DESCRIPTION) LIKE '%SCHOOL%'"
print(pd.DataFrame(execute_query(script)))

# Problem 6 List the type of schools along with the average safety score for each type
script = "DESCRIBE CHICAGO_PUBLIC_SCHOOLS"
print(pd.DataFrame(execute_query(script)))

script = "SELECT `Elementary, Middle, or High School`, AVG(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS GROUP BY `Elementary, Middle, or High School`"
print(pd.DataFrame(execute_query(script)))
# 0  ES  49.5204
# 1  HS  49.6235
# 2  MS  48.0000

# Problem 7 List 5 community areas with highest % of households below poverty line
script = "SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5"
print(pd.DataFrame(execute_query(script)))
# 0           Riverdale
# 1         Fuller Park
# 2           Englewood
# 3      North Lawndale
# 4  West Garfield Park

# Problem 8 Which community area is most crime prone? Display the coumminty area number only.
script = "SELECT COMMUNITY_AREA_NUMBER, COUNT(CASE_NUMBER) FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(*) DESC"
print(pd.DataFrame(execute_query(script))) # Nan = 29, 25 = 27

# Problem 9 Use a sub-query to find the name of the community area with highest hardship index
script = "SELECT COMMUNITY_AREA_NAME, HARDSHIP_INDEX FROM CENSUS_DATA WHERE HARDSHIP_INDEX = (SELECT MAX(HARDSHIP_INDEX) FROM CENSUS_DATA)"
print(pd.DataFrame(execute_query(script))) # 0  Riverdale  98

# Problem 10 Use a sub-query to determine the Community Area Name with most number of crimes?
script = "SELECT COMMUNITY_AREA_NAME FROM CENSUS_DATA WHERE COMMUNITY_AREA_NUMBER IN (SELECT COMMUNITY_AREA_NUMBER FROM CHICAGO_CRIME_DATA GROUP BY COMMUNITY_AREA_NUMBER ORDER BY COUNT(CASE_NUMBER) DESC LIMIT 1)"
print(pd.DataFrame(execute_query(script)))