import pandas as pd

def load_csv(path):
    """Carga un archivo CSV y devuelve un DataFrame."""
    return pd.read_csv(path)