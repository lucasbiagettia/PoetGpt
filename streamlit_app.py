import streamlit as st
from src.model import load_model_and_tokenizer, generate_poem
from src.formatter import preprocess_poem_with_stanzas

# Configuración de la aplicación
st.set_page_config(
    page_title="Generador de Poemas - GPTNeoX",
    layout="centered",
    initial_sidebar_state="auto"
)

# Cargar el modelo y tokenizador
@st.cache_resource
def initialize_model():
    repo_name = "lucasbiagettia/GPTNeoX-spanish_poet"
    return load_model_and_tokenizer(repo_name)

model, tokenizer = initialize_model()

# Título e introducción
st.title("🎨 Generador de Poemas - GPTNeoX")
st.write(
    "Bienvenido a la aplicación de generación de poemas. "
    "Escribe tu poema en el área de texto y presiona **Generar continuación** para que la IA lo complete. "
    "Puedes editar el poema directamente en la misma sección y seguir generando más contenido."
)

# Inicializar el estado del poema
if "current_poem" not in st.session_state:
    st.session_state.current_poem = "La arena me recuerda a\nla nostalgia de la noche"

# Área de texto editable para el poema
st.subheader("📜 Tu poema:")
current_poem = st.text_area(
    "Escribe y edita tu poema aquí:",
    value=st.session_state.current_poem,
    height=300
)

# Botón para generar la continuación
if st.button("🌟 Generar continuación"):
    if current_poem.strip():
        with st.spinner("Generando continuación..."):
            # Formatear la entrada actual del poema
            formatted_input = preprocess_poem_with_stanzas(
                current_poem
            )
            # Generar continuación
            generated_text = generate_poem(model, tokenizer, formatted_input)

        # Actualizar el poema en el estado
        st.session_state.current_poem = generated_text
        st.rerun()  # Volver a renderizar la aplicación con el poema actualizado
    else:
        st.warning("Por favor, escribe algunas líneas para comenzar.")

# Créditos en la barra lateral
st.sidebar.title("💡 Acerca de esta app")
st.sidebar.info(
    "Esta aplicación fue desarrollada para demostrar el poder de los modelos de lenguaje "
    "en la generación de texto creativo. \n\n"
    "Model: [GPTNeoX - Spanish Poet](https://huggingface.co/lucasbiagettia/GPTNeoX-spanish_poet)\n\n"
    "Code: [PoetGpt](https://github.com/lucasbiagettia/PoetGpt)"
)
