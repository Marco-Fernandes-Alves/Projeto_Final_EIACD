import os
import sys
from integracao_processamento import process_data
from analise_exploratoria import run_eda
from identificacao_padroes import run_clustering
from modelos_previsao import run_modeling

def main():
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    try:
        process_data()
        run_eda()
        run_clustering()
        run_modeling()
    except Exception:
        sys.exit(1)

if __name__ == '__main__':
    main()
