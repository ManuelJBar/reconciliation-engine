def normalize_columns(df):
    """Normaliza nombres de columnas a minúsculas."""
    df.columns = df.columns.str.lower()
    return df