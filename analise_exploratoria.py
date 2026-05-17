import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

input_file = "dados_integrados.csv"
output_dir = "outputs/"

def run_eda():
    if not os.path.exists(input_file):
        return

    df = pd.read_csv(input_file)

    # 1. Matriz de Correlação
    plt.figure(figsize=(12, 8))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Matriz de Correlação das Variáveis')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'matriz_correlacao.png'))
    plt.close()

    # 2. Perda de Peso por Dieta (Boxplot simples)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='diet_type', y='weight_change_kg_6m', data=df)
    plt.title('Distribuição da Perda de Peso por Tipo de Dieta')
    plt.ylabel('Alteração de Peso (kg)')
    plt.savefig(os.path.join(output_dir, 'perda_peso_por_dieta.png'))
    plt.close()

    # 3. Perda de Peso por Idade e Sexo (Gráfico de Barras)
    plt.figure(figsize=(10, 6))
    df['age_group'] = pd.cut(df['age'], bins=[0, 30, 50, 100], labels=['Jovem (<30)', 'Adulto (30-50)', 'Sénior (>50)'])
    sns.barplot(x='age_group', y='weight_change_kg_6m', hue='sex', data=df)
    plt.title('Perda de Peso Média por Grupo Etário e Sexo')
    plt.ylabel('Média de Perda de Peso (kg)')
    plt.savefig(os.path.join(output_dir, 'perda_peso_por_idade_sexo.png'))
    plt.close()

    # 4. Impacto da Abordagem do Nutricionista (Boxplot simples em vez de Violin Plot)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='approach', y='weight_change_kg_6m', data=df, palette='Set2')
    plt.title('Perda de Peso por Abordagem do Nutricionista')
    plt.xlabel('Abordagem (Comportamental vs Prescritiva)')
    plt.ylabel('Alteração de Peso (kg)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'impacto_nutricionista.png'))
    plt.close()

    print(f"Análise concluída. Gráficos guardados em: {output_dir}")

if __name__ == "__main__":
    run_eda()
