from database_utils import Database

db = Database()
db_connection = db.connect(database_name="learning_mysql_with_python")

sql = "SELECT AVG(COST/QUANTITY) FROM PETRESCUE WHERE ANIMAL LIKE 'Dog'"
average_cost_of_rescuing_a_dog = db.execute_query(sql)
print(average_cost_of_rescuing_a_dog)

sql = "SELECT DISTINCT(UPPER(ANIMAL)) FROM PETRESCUE"
animal_names_rescue = db.execute_query(sql)
print(animal_names_rescue)

sql = "SELECT * FROM PETRESCUE WHERE ANIMAL = LOWER('Cat')"
rescued_cats_info = db.execute_query(sql)
print(rescued_cats_info)

sql = "SELECT SUM(QUANTITY) FROM PETRESCUE WHERE MONTH(RESCUEDATE) = '05'"
number_of_rescues_in_may = db.execute_query(sql)
print(number_of_rescues_in_may)

sql = "SELECT ID, DATE_ADD(RESCUEDATE, INTERVAL 1 YEAR) FROM PETRESCUE"
expected_date_of_finding_homes_for_rescued_animals = db.execute_query(sql)
print(expected_date_of_finding_homes_for_rescued_animals)

db.close()