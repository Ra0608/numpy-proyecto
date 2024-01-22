import pandas as pd
import matplotlib.pyplot as plt

# Read the DataFrame from the CSV file (replace 'your_data.csv' with the actual file name)
df = pd.read_csv("datos_descargados.csv")

plt.figure(figsize=(12, 8))


plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black', alpha=0.7, label='Age Distribution')

df_anemics = df.groupby('gender')['anemic'].value_counts().unstack()
df_anemics.plot(kind='bar', stacked=True, width=0.8, color=['#ff9999', '#66b3ff'], alpha=0.7, label='Anemics by Gender')


df_diabetics = df.groupby('gender')['diabetic'].value_counts().unstack()
df_diabetics.plot(kind='bar', stacked=True, width=0.8, color=['#ff9999', '#66b3ff'], alpha=0.7, label='Diabetics by Gender')

df_smokers = df.groupby('gender')['smoker'].value_counts().unstack()
df_smokers.plot(kind='bar', stacked=True, width=0.8, color=['#ff9999', '#66b3ff'], alpha=0.7, label='Smokers by Gender')


plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Combined Distributions')
plt.legend()

plt.show()


