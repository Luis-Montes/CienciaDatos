import backend as be  # Importamos la lógica que ya creaste
import streamlit as st

# Configuración de la página web
st.set_page_config(
    page_title="Dashboard de Churn - Predicción de Abandono",
    page_icon="*",
    layout="wide",
)

st.title("Dashboard Inteligente de Retención de Clientes (Churn)")
st.markdown(
    "Aplicación conectada a SQL Server para predecir el riesgo de fuga de clientes mediante Machine Learning."
)

# Cargamos los datos y el modelo desde el backend
with st.spinner("Conectando a SQL Server y entrenando el modelo..."):
    (
        df_clientes, 
        modelo, 
        scaler, 
        fig,
        accuracy,
        precision,
        recall
    )= be.cargar_y_entrenar_modelo()

# ==========================================
# 1. MÉTRICAS PRINCIPALES (KPIs)
# ==========================================
st.subheader("Resumen General")

# Simulamos las predicciones para todo el dataset actual
X_data = df_clientes[["tiempo_en_tienda", "cantidad_compras", "devoluciones"]]
X_scaled = scaler.transform(X_data)
df_clientes["prediccion"] = modelo.predict(X_scaled)
df_clientes["probabilidad_churn"] = (
    modelo.predict_proba(X_scaled)[:, 1] * 100
).round(2)

total_clientes = len(df_clientes)
clientes_riesgo = int(df_clientes["prediccion"].sum())
porcentaje_riesgo = round((clientes_riesgo / total_clientes) * 100, 2)

col1, col2, col3 = st.columns(3)
col1.metric("Total de Clientes Analizados", total_clientes)
col2.metric(
    "Clientes en Alerta de Abandono",
    clientes_riesgo,
    delta_color="inverse",
)
col3.metric("Tasa de Churn Global", f"{porcentaje_riesgo}%")

divider = st.divider()

st.subheader("Métricas de Rendimiento del Modelo (Evaluación)")

m1, m2, m3 = st.columns(3)
m1.metric("Exactitud (Accuracy)", f"{accuracy}%")
m2.metric("Precisión (Precision)", f"{precision}%")
m3.metric("Sensibilidad (Recall)", f"{recall}%")

# Sección de la Matriz de Confusión al lado de una explicación
col_m1, col_m2 = st.columns([1, 1])
with col_m1:
  st.markdown("""
        ### ¿Cómo interpretar estas métricas?
        * **Exactitud:** Porcentaje global de aciertos del modelo.
        * **Precisión:** De las alertas de fuga enviadas, cuántas fueron reales.
        * **Sensibilidad:** Qué tantos clientes en riesgo real fuimos capaces de atrapar.
        * **Algoritmo utilizado:** Regresión Logística.
        * **Validación:** División 80/20 de los datos históricos.
        * **Métrica clave:** Capacidad de identificar correctamente a los clientes con alto riesgo de fuga para evitar pérdidas económicas en la tienda.
    """)
with col_m2:
  st.pyplot(fig)

# ==========================================
# 2. TABLA INTERACTIVA DE CLIENTES
# ==========================================
st.subheader("Listado de Clientes y Probabilidad de Fuga")

# Filtro interactivo en la barra lateral o en pantalla
filtro_riesgo = st.checkbox("Mostrar únicamente clientes en alto riesgo (> 50%)")

if filtro_riesgo:
    df_mostrar = df_clientes[df_clientes["probabilidad_churn"] > 50]
else:
    df_mostrar = df_clientes

st.dataframe(df_mostrar, width="stretch")

# ==========================================
# 3. SIMULADOR DE RIESGO EN VIVO
# ==========================================
st.subheader("Simulador de Riesgo para un Cliente Nuevo")

col_a, col_b, col_c = st.columns(3)
with col_a:
    sim_tiempo = st.number_input(
        "Tiempo en Tienda (minutos)", min_value=0, max_value=1000, value=30
    )
with col_b:
    sim_compras = st.number_input(
        "Cantidad de Compras", min_value=0, max_value=100, value=1
    )
with col_c:
    sim_devoluciones = st.number_input(
        "Cantidad de Devoluciones", min_value=0, max_value=20, value=2
    )

if st.button("Calcular Riesgo de Abandono"):
    # Preparamos el dato ingresado
    input_usuario = [[sim_tiempo, sim_compras, sim_devoluciones]]
    input_scaled = scaler.transform(input_usuario)

    pred_resultado = modelo.predict(input_scaled)[0]
    prob_resultado = (
        modelo.predict_proba(input_scaled)[0][1] * 100
    )  # Probabilidad de la clase 1

    if pred_resultado == 1:
        st.error(
            f"**Alerta Roja:** Este cliente tiene un **{prob_resultado:.2f}%** de probabilidad de abandono."
        )
    else:
        st.success(
            f"**Cliente Seguro:** Este cliente está retenido. Probabilidad de fuga de solo **{prob_resultado:.2f}%**."
        )