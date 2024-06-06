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

# Accessing dataframes
print(employees.iloc[1, 1]) # Expected to be data scientist
print(employees.loc[1:2, "employee_name":"salary"]) # loc can be used with combination of integers and column based headers
employees_v1 = employees.set_index("employee_name")
print(employees_v1.loc["Anna Blue", "position"]) # Expected to be project manager

# List of dictionaries
animes = [
    {
        "title": "Frieren: Beyond Journey's End",
        "studio": "Madhouse",
        "episodes": 22,
        "genres": ("Adventure", "Drama", "Fantasy"),
        "start_aired_date": "2023-09-29",
        "end_aired_date": "2024-03-24"
    },
    {
        "title": "That Time I Got Reincarnated as a Slime",
        "studio": "8bit",
        "episodes": 24,
        "genres": ("Action", "Adventure", "Comedy", "Fantasy"),
        "start_aired_date": "2018-10-02",
        "end_aired_date": "2019-03-19"
    },
    {
        "title": "Undead Unluck",
        "studio": "David Production",
        "episodes": 24,
        "start_aired_date": "2023-10-07",
        "end_aired_date": "2024-03-03"
    }
]

animes_pd = pd.DataFrame(animes)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

print(animes_pd)

# Removes rows with missing data/NaN
animes_pd.dropna(axis=0, inplace=True)
print(animes_pd)

# Renaming columns
animes_pd = animes_pd.rename(columns={
    'title': 'anime_title',
    'studio': 'production_studio',
    'episodes': 'episode_count',
    'genres': 'genre_list'
})
print(animes_pd)

animes_pd.drop(["start_aired_date", "end_aired_date"], axis=1, inplace=True)
print(animes_pd)