import pandas as pd
import os

def load_csv(path):
    """Carga un CSV y valida que exista y tenga contenido."""
    if not os.path.exists(path):
        print(f"❌ ERROR: No se encontró el archivo: {path}")
        return None

    df = pd.read_csv(path)

    if df.empty:
        print(f"❌ ERROR: El archivo está vacío: {path}")
        return None

    print(f"📄 Archivo cargado correctamente: {path} ({len(df)} filas)")
    return df


def normalize_columns(df):
    df.columns = df.columns.str.lower()
    return df


def reconcile(df_a, df_b, key="trade_id"):
    df_a = normalize_columns(df_a)
    df_b = normalize_columns(df_b)

    merged = df_a.merge(
        df_b,
        on=key,
        how="outer",
        suffixes=("_A", "_B"),
        indicator=True
    )

    discrepancies = merged[
        (merged["_merge"] != "both") |
        (merged.filter(regex="_A$") != merged.filter(regex="_B$").values).any(axis=1)
    ]

    return discrepancies


if __name__ == "__main__":
    print("🔍 Iniciando reconciliación...\n")

    df_a = load_csv("data_input/trades_systemA.csv")
    df_b = load_csv("data_input/trades_systemB.csv")

    if df_a is None or df_b is None:
        print("\n❌ Proceso detenido por errores en los archivos de entrada.")
        exit()

    print("\n🔎 Comparando operaciones...\n")
    report = reconcile(df_a, df_b)

    print("📊 RESULTADO DE LA RECONCILIACIÓN:")
    print(report if not report.empty else "✔ No se encontraron discrepancias.")

    output_path = "data_output/reconciliation_report.csv"
    report.to_csv(output_path, index=False)

    print(f"\n💾 Reporte guardado en: {output_path}")
    print("\n✅ Proceso completado.")