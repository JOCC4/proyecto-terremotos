import pandas as pd


def test_dataset_transformado_existe():
    df = pd.read_csv("data/processed/terremotos_transformados.csv")
    assert len(df) > 0


def test_columnas_nuevas_existen():
    df = pd.read_csv("data/processed/terremotos_transformados.csv")
    assert "categoria_magnitud" in df.columns
    assert "categoria_profundidad" in df.columns


def test_no_hay_nulos():
    df = pd.read_csv("data/processed/terremotos_transformados.csv")
    assert df.isnull().sum().sum() == 0
