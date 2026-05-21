import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

input_file = 'dados_integrados.csv'
output_dir = 'outputs/'

def run_clustering():
    if not os.path.exists(input_file):
        return

    df = pd.read_csv(input_file)

    features = ['age', 'baseline_bmi', 'weight_change_kg_6m', 'motivation_score_program', 'mean_adherence_pct']

    X = df[features].dropna()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    df.loc[X.index, 'cluster'] = clusters

    cluster_summary = df.groupby('cluster')[features].mean()
    cluster_summary.to_csv(os.path.join(output_dir, 'perfis_clusters.csv'))

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='age', y='weight_change_kg_6m', hue='cluster', palette='viridis', alpha=0.6)
    plt.title('Identificação de Grupos de Pacientes (Clusters)')
    plt.xlabel('Idade')
    plt.ylabel('Perda de Peso (kg)')
    plt.savefig(os.path.join(output_dir, 'clusters_pacientes.png'))
    plt.close()

if __name__ == '__main__':
    run_clustering()
