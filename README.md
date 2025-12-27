# Reconciliation Engine

Motor de reconciliación de operaciones financieras desarrollado en Python.  
Compara operaciones entre dos sistemas (System A y System B), detecta discrepancias y genera un reporte detallado en formato CSV.

Este proyecto está diseñado como una herramienta ligera y extensible para middle office, control de riesgos, data quality y automatización de procesos financieros.

---

## 🚀 Funcionalidades principales

- **Carga y validación de archivos CSV**
  - Verifica existencia
  - Comprueba que no estén vacíos
  - Muestra número de filas cargadas

- **Normalización de columnas**
  - Convierte nombres a minúsculas para evitar inconsistencias

- **Reconciliación por `trade_id`**
  - Identifica operaciones coincidentes
  - Detecta diferencias de precio, cantidad, ISIN o fecha
  - Señala operaciones faltantes en cada sistema

- **Reporte automático**
  - Genera un archivo CSV con todas las discrepancias
  - Incluye indicador `_merge` para análisis rápido

- **Mensajes claros en consola**
  - Progreso del proceso
  - Resultados
  - Errores de entrada

---

## 📂 Estructura del proyecto

