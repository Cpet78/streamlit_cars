
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df_cars_original = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep = ',')

# Copier le DataFrame original pour conserver la colonne 'continent'
df_cars = df_cars_original.copy()

# Supprimer la colonne 'continent' pour les graphiques
df_cars = df_cars.drop(columns=['continent'])

# Matrice de corrélation
corr_matrix = df_cars.corr()

# Tracer la matrice de corrélation
fig_corr = plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matrice de corrélation')
st.pyplot(fig_corr)

# Histogramme
fig_hist = plt.figure(figsize=(10, 8))
df_cars.hist()
plt.suptitle('Histogrammes des variables', x=0.5, y=0.92)
st.pyplot(fig_hist)

# Relation entre variables
fig_pairplot = sns.pairplot(df_cars, vars=['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60'])
plt.suptitle('Nuages de points pour les paires de variables sélectionnées', x=0.5, y=1.02)
st.pyplot(fig_pairplot)

# Sélectionner la région à filtrer
regions = df_cars_original['continent'].unique().tolist()  # Récupérer les valeurs uniques de la colonne 'continent' dans le DataFrame original
regions.insert(0, 'Toutes')
selected_region = st.selectbox('Sélectionner une région:', regions)

# Filtrer les données par région
if selected_region == 'Toutes':
    filtered_df = df_cars_original  # Utiliser le DataFrame original avec la colonne 'continent' pour le filtrage
else:
    filtered_df = df_cars_original[df_cars_original['continent'] == selected_region]