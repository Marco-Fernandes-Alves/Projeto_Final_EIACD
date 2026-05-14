import pandas as pd
import numpy as np
import os

base_path = "data/"
output_file = "dados_integrados.csv"

def process_data():
    pacientes = pd.read_csv(os.path.join(base_path, "pacientes.csv"))
    dietas = pd.read_csv(os.path.join(base_path, "dietas.csv"))
    nutricionistas = pd.read_csv(os.path.join(base_path, "nutricionistas.csv"))
    resultados = pd.read_csv(os.path.join(base_path, "resultados.csv"))

    df = resultados.merge(pacientes, on="patient_id", how="left")
    df = df.merge(dietas, on="diet_id", how="left")
    df = df.merge(nutricionistas, on="nutritionist_id", how="left")

    df['sex'] = df['sex'].str.strip().str.upper()
    df['sex'] = df['sex'].replace({'FEMALE': 'F', 'MALE': 'M'})
    df['approach'] = df['approach'].str.strip().str.capitalize()

    redundant = ['bmi_redundant', 'experience_years', 'total_macros', 'adherence_ratio']

    df = df.drop(columns=[c for c in redundant if c in df.columns])
    df['fiber_target_g'] = df['fiber_target_g'].fillna(df.groupby('diet_type')['fiber_target_g'].transform('median'))
    df['motivation_score'] = df['motivation_score'].fillna(df['motivation_score'].median())
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    process_data()
