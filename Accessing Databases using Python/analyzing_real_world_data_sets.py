import pandas as pd
import sqlite3
import requests
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Create sql connection
conn = sqlite3.connect("chicago_socioeconomic.db")
cur = conn.cursor()

# Fetch and save the csv file
url = "https://data.cityofchicago.org/resource/jcxq-k9xf.csv"
response = requests.get(url)
path = os.path.join(os.getcwd(), "chicago_socioeconomic.csv")

with open(path, "wb") as file:
    file.write(response.content)

data = pd.read_csv("chicago_socioeconomic.csv")

# Expanding dataframe view
pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

# Converting data to SQL
data.to_sql("chicago_socioeconomic_data", conn, if_exists='replace', index=False)
chicago_socioeconomic_df = pd.read_sql("SELECT * FROM chicago_socioeconomic_data", conn)
print(chicago_socioeconomic_df.head())
print(chicago_socioeconomic_df.describe(include="all")) # will provide summary statistics in numeric and non-numeric column

# How many rows are in the dataset?
print(chicago_socioeconomic_df.index)
print(pd.read_sql("SELECT COUNT(*) FROM chicago_socioeconomic_data", conn))

# How many community areas in Chicago have a hardship index greater than 50.0
print(chicago_socioeconomic_df[chicago_socioeconomic_df["hardship_index"] > 50.0].agg({"ca": "count"}))
print(pd.read_sql("SELECT COUNT(ca) FROM chicago_socioeconomic_data WHERE hardship_index > 50", conn))

# What is the maximum value of hardship index in this dataset?
print(chicago_socioeconomic_df[["hardship_index"]].max())
print(pd.read_sql("SELECT MAX(hardship_index) FROM chicago_socioeconomic_data", conn))

# Which community area has the highest hardship index?
print(chicago_socioeconomic_df.sort_values("hardship_index", ascending=False)["community_area_name"].head(1))
print(chicago_socioeconomic_df.at[chicago_socioeconomic_df["hardship_index"].idxmax(), "community_area_name"])
print(pd.read_sql("SELECT community_area_name FROM chicago_socioeconomic_data WHERE hardship_index IN (SELECT MAX(hardship_index) FROM chicago_socioeconomic_data)", conn))
print(pd.read_sql("SELECT community_area_name FROM chicago_socioeconomic_data ORDER BY hardship_index DESC LIMIT 1", conn))

# Which Chicago community areas have per-capita incomes greater than $60,000
print(chicago_socioeconomic_df[chicago_socioeconomic_df["per_capita_income_"] > 60000][["community_area_name"]])
print(pd.read_sql("SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000", conn))

# Create a scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between two variables
scatter_plot = sns.jointplot(x="per_capita_income_", y="hardship_index", data=chicago_socioeconomic_df)
plt.show()

chicago_socioeconomic_df.plot(x="per_capita_income_", y="hardship_index", kind="scatter")
plt.show()

# There is a negative correlation between income and hardship

conn.close()