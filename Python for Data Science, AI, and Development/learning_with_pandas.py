import pandas as pd

even = [2, 4, 6, 8, 10]
evenSeries = pd.Series(even)
print(evenSeries)

print(evenSeries[1])
print(evenSeries.iloc[1])

employeeFile = pd.read_csv('employees.csv', index_col=0)
employees = pd.DataFrame(employeeFile)

print("Shape of the employees dataframe", employees.shape)
print("Summary statistics of the employees dataframe (salary per month)", employees.describe())
print("Information about the employees dataframe in column and row format")
employees.info()
print("First 5 elements of the employees dataframe")
print(employees.head())
print("Last 5 elements of the employees dataframe")
print(employees.tail())
print("Mean salary of employees")
print(employees["salary"].mean())
print("Maximum salary given to an employee per month")
print(employees["salary"].max())
print("Minimum salary given to an employee per month")
print(employees["salary"].min())
print("Total salary given to the employees by the company per month")
print(employees["salary"].sum())
print("Sorted employees dataframe by salary from highest to lowest")
print(employees.sort_values("salary", ascending=False))
print("Average Salary per month by Position")
print(employees.groupby("position")["salary"].agg("mean"))

def getAnnualSalary(monthSalary):
    return monthSalary * 12

employees['annual_salary'] = employees['salary'].apply(getAnnualSalary)
print("Average Annual Salary per Position")
print(employees.groupby("position")['annual_salary'].mean())

print(employees.columns)
employees = employees.rename(columns={"name": "employee_name"})
print(employees.columns)