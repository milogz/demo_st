import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Demo Privado", page_icon="🔒")


# --- FUNCIÓN DE AUTENTICACIÓN ---
def check_password():
    """Retorna `True` si el usuario tiene la clave correcta."""

    def password_entered():
        """Verifica si la clave ingresada coincide con la guardada en secrets."""
        if st.session_state["password"] == st.secrets["password_acceso"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Borrar clave por seguridad
        else:
            st.session_state["password_correct"] = False

    # Si ya está validado, retornar True
    if st.session_state.get("password_correct", False):
        return True

    # Mostrar input de contraseña
    st.text_input(
        "Ingresa la contraseña para acceder:", 
        type="password", 
        on_change=password_entered, 
        key="password"
    )
    
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 Contraseña incorrecta")
        
    return False


# --- LÓGICA PRINCIPAL (SOLO SE EJECUTA SI HAY LOGIN) ---
if check_password():
    
    # 1. TÍTULO Y BARRA LATERAL
    st.title("📊 Tablero de Control Demo")
    st.sidebar.header("Configuración")
    st.success("¡Bienvenido! Has iniciado sesión correctamente.")

    # 2. INTERACTIVIDAD (WIDGETS)
    # Esto reemplaza a las variables fijas en tu código original
    num_puntos = st.sidebar.slider("Número de puntos", 10, 100, 50)
    color_grafico = st.sidebar.selectbox("Color del gráfico", ["blue", "red", "green"])

    # 3. GENERACIÓN DE DATOS (Simulando tu lógica de negocio)
    data = pd.DataFrame({
        'Mes': pd.date_range(start='2025-01-01', periods=num_puntos),
        'Valor': np.random.randn(num_puntos).cumsum()
    })

    # 4. VISUALIZACIÓN (Matplotlib, igual que en tu proyecto)
    st.subheader(f"Proyección Aleatoria ({num_puntos} días)")
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(data['Mes'], data['Valor'], color=color_grafico, marker='o', markersize=3)
    ax.set_title("Evolución Simulada")
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Mostrar el gráfico en la web
    st.pyplot(fig)

    # 5. MOSTRAR DATOS
    with st.expander("Ver datos crudos"):
        st.dataframe(data)