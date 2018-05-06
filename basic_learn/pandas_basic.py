#! /usr/bin/env python

import pandas as pd

city_names = pd.Series(['shang hai', 'nan jing', 'su zhou'])
population = pd.Series([1000, 2000, 3000])
population = population/1000
city_population = pd.DataFrame({'City Name':city_names, 'Population': population})
print(city_population.describe())
print(city_names)
print(population)
print(city_population)
print(city_population['City Name'])
