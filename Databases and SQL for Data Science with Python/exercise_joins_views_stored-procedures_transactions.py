import mysql.connector as mysql
import pandas as pd

connection = mysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="",
                           database="learning_mysql_with_python")

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

def execute_query(script):
    if connection.is_connected() == False:
        connection.reconnect(attempts=3, delay=5)
    Cursor = connection.cursor()
    Cursor.execute(script)
    result = Cursor.fetchall()
    Cursor.close()
    return result

sql_script = "SELECT SCHOOLS.NAME_OF_SCHOOL, SCHOOLS.COMMUNITY_AREA_NAME, SCHOOLS.AVERAGE_STUDENT_ATTENDANCE FROM CHICAGO_PUBLIC_SCHOOLS SCHOOLS LEFT JOIN CHICAGO_SOCIOECONOMIC_DATA SOCIODATA ON SCHOOLS.COMMUNITY_AREA_NAME = SCHOOLS.COMMUNITY_AREA_NAME WHERE SOCIODATA.HARDSHIP_INDEX = 98"
print(pd.DataFrame(execute_query(sql_script)))

sql_script = "SELECT CRIME.CASE_NUMBER, CRIME.PRIMARY_TYPE, SCHOOLS.COMMUNITY_AREA_NAME FROM CHICAGO_CRIME CRIME INNER JOIN CHICAGO_PUBLIC_SCHOOLS SCHOOLS ON CRIME.COMMUNITY_AREA_NUMBER = SCHOOLS.COMMUNITY_AREA_NUMBER WHERE UPPER(CRIME.LOCATION_DESCRIPTION) LIKE UPPER('%SCHOOL%')"
print(pd.DataFrame(execute_query(sql_script)))

sql_script = """CREATE VIEW IF NOT EXISTS chicago_public_schools_list AS
                SELECT NAME_OF_SCHOOL AS School_Name,
                       Safety_Icon AS Safety_Rating,
                       Family_Involvement_Icon AS Family_Rating,
                       Environment_Icon AS Environment_Rating,
                       Leaders_Icon AS Leaders_Rating,
                       Teachers_Icon AS Teachers_Rating
                FROM CHICAGO_PUBLIC_SCHOOLS"""
execute_query(sql_script)
print(pd.DataFrame(execute_query("SELECT * FROM chicago_public_schools_list")))

# NOTE: IF THERE IS AN UPDATE STATEMENT, THERE SHOULD BE A WORD CALLED COMMIT SO THAT IT WOULD
sql_script = """CREATE PROCEDURE IF NOT EXISTS UPDATE_LEADERS_SCORE(IN in_School_ID INT, IN in_Leader_Score INT)
                BEGIN
                    START TRANSACTION;
                    UPDATE CHICAGO_PUBLIC_SCHOOLS 
                    SET Leaders_Score = in_Leader_Score 
                    WHERE School_ID = in_School_ID;
                    
                    IF in_Leader_Score >= 80 AND in_Leader_Score <= 99 THEN
                        UPDATE CHICAGO_PUBLIC_SCHOOLS SET Leaders_Icon = 'Very Strong' WHERE School_ID = in_School_ID;
                    ELSEIF in_Leader_Score >= 60 AND in_Leader_Score <= 79 THEN
                        UPDATE CHICAGO_PUBLIC_SCHOOLS SET Leaders_Icon = 'Strong' WHERE School_ID = in_School_ID;
                    ELSEIF in_Leader_Score >= 40 AND in_Leader_Score <= 59 THEN
                        UPDATE CHICAGO_PUBLIC_SCHOOLS SET Leaders_Icon = 'Average' WHERE School_ID = in_School_ID;
                    ELSEIF in_Leader_Score >= 20 AND in_Leader_Score <= 39 THEN
                        UPDATE CHICAGO_PUBLIC_SCHOOLS SET Leaders_Icon = 'Weak' WHERE School_ID = in_School_ID;
                    ELSEIF in_Leader_Score >= 0 AND in_Leader_Score <= 19 THEN
                        UPDATE CHICAGO_PUBLIC_SCHOOLS SET Leaders_Icon = 'Very Weak' WHERE School_ID = in_School_ID;
                    ELSE
                        ROLLBACK;
                    END IF;
                    
                    COMMIT;
                END"""
execute_query(sql_script)

sql_script = "CALL UPDATE_LEADERS_SCORE(609964,50)"
execute_query(sql_script)

