
# Generador de Poemas con GPTNeoX

Bienvenido al **Generador de Poemas con GPTNeoX**, una aplicación interactiva desarrollada en Streamlit que permite crear poemas de manera colaborativa con un modelo de lenguaje entrenado específicamente para poesía en español. ¡Escribe tus primeras líneas y deja que la inteligencia artificial complete tu obra!

## 🚀 Características

- **Colaborativo**: Permite a los usuarios editar y continuar generando poesía en un solo campo de texto.
- **Personalizado**: Utiliza un modelo GPTNeoX entrenado en un corpus específico de poesía en español.
- **Fluido**: Controla el tamaño del contexto pasado al modelo (máximo 128 tokens) para garantizar una experiencia eficiente y contextual.

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Streamlit**: Framework para crear la interfaz web interactiva.
- **Transformers**: Biblioteca de Hugging Face para el manejo del modelo de lenguaje.
- **PyTorch**: Backend utilizado por el modelo para inferencia.

## 📂 Estructura del Proyecto

```
poetry_generator_app/
│
├── app.py                   # Archivo principal de la aplicación Streamlit
├── requirements.txt         # Lista de dependencias del proyecto
├── README.md                # Documentación del proyecto
│
├── src/                     # Código fuente modularizado
│   ├── __init__.py          # Indica que es un paquete Python
│   ├── model.py             # Funciones para cargar el modelo y generar texto
│   ├── formatter.py         # Lógica de formateo y preprocesamiento del texto
│   ├── config.py            # Configuración del modelo y parámetros de generación
│
├── assets/                  # Recursos adicionales (opcional)
│   ├── examples/            # Ejemplos de entrada y salida del modelo
│   └── images/              # Imágenes para la documentación o app
│
└── tests/                   # Pruebas unitarias del código
    ├── __init__.py          # Indica que es un paquete Python
    ├── test_model.py        # Pruebas para la generación de texto
    ├── test_formatter.py    # Pruebas para el preprocesamiento del texto
    └── test_app.py          # Pruebas de integración con Streamlit (opcional)
```

## 📋 Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior.
- Pip (Administrador de paquetes de Python).
- [CUDA](https://developer.nvidia.com/cuda-toolkit) (opcional, si usas GPU).

## ⚙️ Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/poetry_generator_app.git
   cd poetry_generator_app
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scriptsctivate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación:**
   ```bash
   streamlit run app.py
   ```

## 🧠 Modelo de Lenguaje

Este proyecto utiliza el modelo `GPTNeoX-spanish_poet`, alojado en [Hugging Face](https://huggingface.co). El modelo está optimizado para generar texto creativo en español, con un enfoque en estructuras poéticas.

## 🖼️ Ejemplo de Interacción

1. **Entrada inicial del usuario:**
   ```
   En la penumbra del bosque
   el viento susurra su canción.
   ```

2. **Texto generado:**
   ```
   En la penumbra del bosque
   el viento susurra su canción.

   Las hojas bailan en el aire,
   reflejos del alma en soledad.

   Un río murmura entre las piedras,
   llevando secretos hacia el mar.
   ```

3. **Editar y continuar generando:**
   El usuario puede añadir más líneas al poema generado y solicitar nuevas continuaciones.

## 🧪 Pruebas

Ejecuta las pruebas para verificar la funcionalidad del proyecto:

```bash
pytest tests/
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añade nueva funcionalidad'`).
4. Haz un push a tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## 📜 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

## ✨ Créditos

Desarrollado por [Tu Nombre](https://github.com/tu_usuario).

Modelo basado en `GPTNeoX` entrenado en [Hugging Face](https://huggingface.co).
