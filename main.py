import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn")

# data taken from https://github.com/owid/co2-data
data = pd.read_csv("data.csv").fillna(0)
year = np.unique(data['year'].values)

asia = [0.0]*(271 - len((data[data['country'] == "Asia"]['co2']).tolist())) + (data[data['country'] == "Asia"]['co2']).tolist()
# asia = (data[data['country'] == "Asia"]['co2']).tolist()
# asia = [0]*(270 - len(asia)) + asia
na = [0.0]*(271 - len((data[data['country'] == "North America"]['co2']).tolist())) + (data[data['country'] == "North America"]['co2']).tolist()
sa = [0.0]*(271 - len((data[data['country'] == "South America"]['co2']).tolist())) + (data[data['country'] == "South America"]['co2']).tolist()
eu = [0.0]*(271 - len((data[data['country'] == "Europe"]['co2']).tolist())) + (data[data['country'] == "Europe"]['co2']).tolist()
afr = [0.0]*(271 - len((data[data['country'] == "Africa"]['co2']).tolist())) + (data[data['country'] == "Africa"]['co2']).tolist()
oce = [0.0]*(271 - len((data[data['country'] == "Oceania"]['co2']).tolist())) + (data[data['country'] == "Oceania"]['co2']).tolist()
ant = [0.0]*(271 - len((data[data['country'] == "Antarctica"]['co2']).tolist())) + (data[data['country'] == "Antarctica"]['co2']).tolist()

palette = sns.color_palette("Spectral", 7).as_hex()
colors = ','.join(palette)
labels = ("Asia", "North America", "South America", "Europe", "Africa", "Oceania", "Antarctica")

plt.figure(figsize=(10, 6))
plt.stackplot(year, asia, na, sa, eu, afr, oce, ant, colors=colors, labels=labels)
plt.title("Annual Production-Based CO2 Emissions by Continent from 1750-2020")
plt.xlabel("Year")
plt.ylabel("Production-Based CO2 Emissions (in MMT)")
plt.legend(loc="upper left", shadow=True, ncol=1)
plt.xticks(np.arange(1750, 2021, step=10), rotation=45)
plt.margins(x=0)

plt.show()
