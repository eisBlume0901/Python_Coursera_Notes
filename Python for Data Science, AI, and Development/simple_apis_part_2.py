import numpy as np
import pandas as pd

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

tables = pd.read_html(URL) # pip install lxml first

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited
pd.set_option('display.max_colwidth', None)  # None means unlimited

gdp_df = pd.DataFrame(tables[3])
print(gdp_df)

gdp_df.columns = range(gdp_df.shape[1])
print(gdp_df)

# Exercise 1
# TOP 10 largest economies in the world
gdp_df.rename(columns={
    0: "Country",
    2: "GDP (Million USD)"
}, inplace=True)
print(gdp_df.iloc[1:11, [0, 2]]) # Rows 1 to 11 and columns 0 and 2

# Exercise 2
# Converting Millions to Billions and round it off to 2 decimals
gdp_df["GDP (Million USD)"] = gdp_df["GDP (Million USD)"].replace('—', np.nan)
gdp_df["GDP (Million USD)"] = gdp_df["GDP (Million USD)"].astype(float)
gdp_df[["GDP (Million USD)"]] = gdp_df[["GDP (Million USD)"]] / 1000
gdp_df[["GDP (Million USD)"]] = np.round(gdp_df[["GDP (Million USD)"]], 2)
gdp_df.rename(columns={
    "GDP (Million USD)": "GDP (Billion USD)"
}, inplace=True)
print(gdp_df.iloc[1:11, [0, 2]])

largest_economies_by_country = gdp_df.iloc[1:11, [0, 2]]
largest_economies_by_country.to_csv('Largest_economies.csv')