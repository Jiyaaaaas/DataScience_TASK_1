import pandas as pd
import matplotlib.pyplot as plt
import os

folder = "API_SP.POP.TOTL_DS2_en_csv_v2_40826"

for file in os.listdir(folder):
    if file.startswith("API_SP.POP.TOTL") and file.endswith(".csv"):
        file_path = os.path.join(folder, file)

df = pd.read_csv(file_path, skiprows=4)

world_data = df[df["Country Name"] == "World"]

year_columns = [col for col in world_data.columns if col.isdigit()]

year_columns = [year for year in year_columns if int(year) <= 2026]

population = world_data[year_columns].T
population = population.rename(columns={population.columns[0]: "Population"})
population.index = population.index.astype(int)
population = population.dropna()

plt.figure(figsize=(14,6))
plt.bar(population.index, population["Population"])
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Over the Years")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
