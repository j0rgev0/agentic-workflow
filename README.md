# 🎮 Generador de Artículos sobre Videojuegos con IA

Este proyecto es una aplicación desarrollada en Python con Streamlit y CrewAI, que permite generar artículos detallados sobre videojuegos a partir de un tema o palabra clave proporcionada por el usuario. Utiliza un flujo de agentes inteligentes para planificar, redactar y editar el contenido de forma automática.

## 🚀 Características
- **Agente Planificador:** Recopila información relevante y estructura el contenido.
- **Agente Escritor:** Genera un artículo atractivo basado en la planificación.
- **Agente Editor:** Revisa y mejora el artículo final.
- **Noticias en Tiempo Real:** Usa la API de NewsAPI para obtener noticias recientes sobre videojuegos.
- **Interfaz Interactiva:** Desarrollada con Streamlit para una experiencia de usuario fluida.

## 🛠️ Requisitos
- Python 3.8+
- Dependencias listadas en `requirements.txt`

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Configurar variables de entorno
Crea un archivo `.env` con tus claves de API:
```
OPENAI_API_KEY=tu_clave_openai
NEWS_API_KEY=tu_clave_newsapi
```

### Ejecutar la aplicación
```bash
streamlit run app.py
```

## 📂 Estructura del Proyecto
```
📦generador-articulos-videojuegos
 ┣ 📂.streamlit
 ┣ 📂assets
 ┣ 📂components
 ┣ 📜app.py
 ┣ 📜requirements.txt
 ┣ 📜README.md
 ┗ 📜.env
```

## 🤖 Tecnologías Utilizadas
- **Python**: Lenguaje principal.
- **Streamlit**: Para la interfaz de usuario.
- **CrewAI**: Para la gestión de agentes y tareas.
- **Langchain**: Integración con el modelo GPT-4o de OpenAI.
- **Requests**: Para obtener noticias desde la API de NewsAPI.

## 📈 Flujo de Agentes
1. **Planificador**: Analiza el tema y recopila información.
2. **Escritor**: Redacta el artículo basado en el plan.
3. **Editor**: Revisa y optimiza el contenido final.

## 📄 Ejemplo de Uso
Al ingresar el tema "The Legend of Zelda", la aplicación:
1. Muestra noticias recientes sobre el juego.
2. Genera un plan de contenido.
3. Escribe un artículo completo.
4. Realiza una revisión del texto y presenta el artículo final.

## 🧑‍💻 Contribución
Las contribuciones son bienvenidas. Haz un fork del repositorio, crea una rama y abre un pull request.

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

