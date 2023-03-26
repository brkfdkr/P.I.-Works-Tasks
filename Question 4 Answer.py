import pandas as pd
import numpy as np

df = pd.read_csv("country_vaccination_stats.csv",na_values="NaN")

#Finding minimum vaccinations per country
min_vac_per_country = df.groupby("country")["daily_vaccinations"].min()
min_vac_per_country = min_vac_per_country.fillna(0)

#Splitting data to missing and non missing part
missing_data = df[df.daily_vaccinations.isna()] 
df = df.dropna(axis=0)

#With missing data Groupby country and merge with minimums
missing_data = missing_data.merge(min_vac_per_country,on="country",how="inner").drop("daily_vaccinations_x",axis=1)
missing_data.rename(columns = {'daily_vaccinations_y':'daily_vaccinations'}, inplace = True)

#Concat fixed missing data and non missing data 
df = pd.concat([df,missing_data])
print(df.head())
