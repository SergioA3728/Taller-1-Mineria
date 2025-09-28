

from __future__ import annotations

import pandas as pd
import numpy as np
import random
from pathlib import Path
from typing import Dict, List

RUTA_CRUDO = "Dataset_desercion_estudiantil.csv"
RUTA_LIMPIO = "Dataset_desercion_estudiantil_limpio.csv"

def generar_dataset(
    n: int = 500,
    seed: int = 42,
    frac_null: float = 0.05,
    columnas_nulos: List[str] | None = None,
    outliers_conf: Dict[str, Dict[str, List[float]]] | None = None,
) -> pd.DataFrame:
    """Genera el dataset crudo con nulos y outliers.

    Args:
        n: número de registros (>=500)
        seed: semilla reproducible
        frac_null: fracción aproximada de nulos a insertar en cada columna objetivo
        columnas_nulos: columnas sobre las que insertar nulos (default predefinido)
        outliers_conf: configuración de outliers por columna {col: {'high': [...], 'low': [...]}}
    """
    assert n >= 500, "El dataset debe tener al menos 500 registros."
    np.random.seed(seed)
    random.seed(seed)

    # Variables demográficas / académicas / financieras
    edad = np.random.randint(16, 30, n)
    genero = np.random.choice(['M', 'F'], n, p=[0.48, 0.52])
    lugar_origen = np.random.choice(
        ['Soledad', 'Sabanalarga', 'Sabana Grande', 'Baranoa', 'Barranquilla'],
        n,
        p=[0.12, 0.15, 0.10, 0.08, 0.55]
    )
    prom_bach = np.round(np.random.uniform(2.0, 5.0, n), 2)
    icfes = np.round(np.random.uniform(200, 500, n), 0)
    notas_sem1 = np.round(np.random.uniform(2.0, 5.0, n), 2)
    estrato = np.random.choice([1, 2, 3, 4, 5, 6], n, p=[0.18, 0.32, 0.28, 0.12, 0.07, 0.03])
    beca = np.random.choice(['Si', 'No'], n, p=[0.25, 0.75])
    icetex = np.random.choice(['Si', 'No'], n, p=[0.35, 0.65])

    # Probabilidad de deserción (modelo heurístico)
    base_riesgo = (
        (prom_bach < 3.0).astype(int) * 0.35 +
        (notas_sem1 < 3.0).astype(int) * 0.40 +
        (beca == 'No').astype(int) * 0.10 +
        (icetex == 'Si').astype(int) * 0.08 +
        (estrato <= 2).astype(int) * 0.10
    )
    prob_desercion = np.clip(0.05 + base_riesgo, 0, 0.95)
    desercion = np.where(np.random.uniform(0, 1, n) < prob_desercion, 'Si', 'No')

    df = pd.DataFrame({
        'Edad': edad,
        'Genero': genero,
        'Lugar Origen': lugar_origen,
        'Promedio del Bachiderato': prom_bach,
        'ICFES': icfes,
        'Notas Semestre #1': notas_sem1,
        'Estrato': estrato,
        'Beca': beca,
        'Credito Academico': icetex,
        'Desercion': desercion
    })

    # Inserción de nulos reproducible
    if columnas_nulos is None:
        columnas_nulos = ['Promedio del Bachiderato', 'Notas Semestre #1', 'Estrato']
    for i, col in enumerate(columnas_nulos):
        if col not in df.columns:
            continue
        m = int(np.floor(frac_null * n))
        rng = np.random.default_rng(seed + 123 + i)
        idx = rng.choice(df.index, size=m, replace=False)
        df.loc[idx, col] = np.nan

    # Configuración outliers
    if outliers_conf is None:
        outliers_conf = {
            'Promedio del Bachiderato': {'high': [10], 'low': [0.5]},
            'Edad': {'high': [45, 52], 'low': [14]},
            'ICFES': {'high': [700], 'low': [120]},
            'Notas Semestre #1': {'high': [9.5], 'low': [0.8]},
        }

    # Inserción determinista de outliers
    for col, spec in outliers_conf.items():
        if col not in df.columns:
            continue
        for side, valores in spec.items():
            for v in valores:
                # Índice pseudo-determinista
                idx = hash(f"{col}-{v}-{seed}") % n
                df.at[idx, col] = v

    return df

def imputar_basico(df: pd.DataFrame) -> pd.DataFrame:
    """Crea una copia imputada (mediana numéricos, moda categóricos) con indicadores *_faltante."""
    df_imp = df.copy()
    cols_null = df_imp.columns[df_imp.isna().any()].tolist()
    for c in cols_null:
        df_imp[c + '_faltante'] = df_imp[c].isna().astype(int)
        if pd.api.types.is_numeric_dtype(df_imp[c]):
            df_imp[c] = df_imp[c].fillna(df_imp[c].median())
        else:
            df_imp[c] = df_imp[c].fillna(df_imp[c].mode().iloc[0])
    return df_imp

def main():
    if Path(RUTA_CRUDO).exists():
        df = pd.read_csv(RUTA_CRUDO)
        print(f"Cargado dataset existente: {RUTA_CRUDO} ({len(df)} filas)")
    else:
        df = generar_dataset()
        df.to_csv(RUTA_CRUDO, index=False)
        print(f"Generado {RUTA_CRUDO} con {len(df)} filas")

    # Crear versión limpia/imputada
    df_imp = imputar_basico(df)
    df_imp.to_csv(RUTA_LIMPIO, index=False)
    print(f"Guardado {RUTA_LIMPIO} con imputaciones básicas")

    # Resumen rápido en consola
    print("\nResumen nulos crudo:")
    print(df.isna().sum()[df.isna().sum()>0])
    print("\nEjemplo primeras filas crudo:")
    print(df.head(3))
    print("\nOutliers (valores extremos presentes):")
    for col in ['Promedio del Bachiderato','Edad','ICFES','Notas Semestre #1']:
        if col in df.columns:
            extremos = df[(df[col] < df[col].quantile(0.01)) | (df[col] > df[col].quantile(0.99))][col]
            if not extremos.empty:
                print(f" - {col}: muestras -> {extremos.unique()[:6]}")

if __name__ == "__main__":  # pragma: no cover
    main()
