import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

input_file = 'dados_integrados.csv'
output_dir = 'outputs/'

def run_modeling():
    if not os.path.exists(input_file):
        return

    df = pd.read_csv(input_file)

    target = 'weight_change_kg_6m'
    categorical_cols = ['sex', 'diet_type', 'approach', 'diet_name', 'specialty']

    df_model = pd.get_dummies(df, columns=[c for c in categorical_cols if c in df.columns], drop_first=True)

    X = df_model.select_dtypes(include=[np.number, bool]).copy()
    to_remove = ['patient_id', 'diet_id', 'nutritionist_id', 'program_id', 'record_created_at', target, 'age_group']
    X = X.drop(columns=[c for c in to_remove if c in X.columns])
    y = df_model[target]
    mask = ~y.isna() & ~X.isna().any(axis=1)
    X, y = X[mask], y[mask]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
    }

    results = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results.append({
            'Model': name,
            'MAE': mean_absolute_error(y_test, y_pred),
            'R2': r2_score(y_test, y_pred)
        })

    pd.DataFrame(results).to_csv(os.path.join(output_dir, 'comparacao_modelos.csv'), index=False)
    rf = models['Random Forest']
    importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

    plt.figure(figsize=(10, 8))
    importances.head(15).plot(kind='barh')
    plt.title('Importância das Variáveis')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'importancia_variaveis.png'))
    plt.close()

if __name__ == '__main__':
    run_modeling()
