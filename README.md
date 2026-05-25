# Sistema de Análise e Previsão de Perda de Peso

Este projeto foi desenvolvido para a unidade curricular de Introdução à Análise e Ciência de Dados (IACD). O objetivo é analisar dados de pacientes, dietas e intervenções nutricionais para identificar padrões de sucesso na perda de peso e prever resultados futuros utilizando Machine Learning.

## Estrutura do Projeto

```text
Trabalho_Final/
├── main.py
├── integracao_processamento.py
├── analise_exploratoria.py
├── identificacao_padroes.py
├── modelos_previsao.py
├── requirements.txt
├── README.md
├── data/
│   ├── diets.csv
│   ├── nutritionists.csv
│   ├── outcomes.csv
│   └── patients.csv
├── outputs/
│   ├── clusters_pacientes.png
│   ├── comparacao_modelos.csv
│   ├── impacto_nutricionista.png
│   ├── importancia_variaveis.png
│   ├── matriz_correlacao.png
│   ├── perda_peso_por_dieta.png
│   ├── perda_peso_por_idade_sexo.png
│   └── perfis_clusters.csv
└── codigo_comentado/
    ├── analise_exploratoria.md
    ├── identificacao_padroes.md
    ├── integracao_processamento.md
    └── modelos_previsao.md
```

## Como Executar

### Pré-requisitos
Certifique-se de que tem o Python instalado e as dependências necessárias listadas no `requirements.txt`.

### Instalação e Execução
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o pipeline completo:
   ```bash
   python main.py
   ```

## Fases do Pipeline

O projeto está dividido em 4 fases lógicas:
1.  **Integração e Limpeza:** Consolidação de dados e normalização de categorias.
2.  **Análise Exploratória:** Geração de matrizes de correlação e gráficos de distribuição.
3.  **Segmentação:** Agrupamento de pacientes em 4 perfis distintos com base em adesão e motivação.
4.  **Modelagem:** Previsão de perda de peso com avaliação de métricas (MAE e R²).

## Resultados Obtidos

*   **Melhor Modelo:** Random Forest Regressor com R² de aproximadamente 0.90.
*   **Insights:** A adesão à dieta e a pontuação de motivação foram identificadas como os fatores mais críticos para o sucesso do programa.

---
**Data:** Maio de 2026