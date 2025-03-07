import os
import requests
import streamlit as st
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew 
from crewai.tools import tool

# Configuración de la API Key
model = ChatOpenAI(
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o",
    streaming=True,
    temperature=0.7
)

news_api_key = os.getenv("NEWS_API_KEY")

@tool("get_game_news")
def get_game_news(topic: str) -> list:
    """
    Obtiene las últimas noticias sobre videojuegos desde la API de NewsAPI.
    """
    url = f"https://newsapi.org/v2/everything?q={topic} videojuego&apiKey={news_api_key}&pageSize=5"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [
                f"🕹️ **{article['title']}** - {article['source']['name']}\n"
                f"*{article['description']}*\n[Leer más]({article['url']})"
                for article in articles
            ]
        else:
            return []
    except requests.exceptions.RequestException as e:
        return [f"Error al obtener noticias: {str(e)}"]

# Crear la aplicación en Streamlit
st.title("🎮 Generador de Artículos sobre Videojuegos con IA")
st.markdown("Ingresa un **videojuego** o **tema relacionado** y observa cómo cada agente contribuye a la creación del artículo.")

# Entrada de usuario
topic = st.text_input("📌 Tema del artículo sobre videojuegos:", "")

if topic:
    with st.spinner("⏳ Generando contenido..."):

        # Definir agentes
        planner = Agent(
            role="📊 Planificador",
            goal=f"Planificar contenido relevante sobre videojuegos: {topic}",
            backstory="Recopilas información y creas un esquema del contenido.",
            allow_delegation=False,
            llm=model,
            tools=[get_game_news],
            verbose=True
        )

        writer = Agent(
            role="✍️ Escritor",
            goal=f"Redactar un artículo atractivo sobre videojuegos: {topic}",
            backstory="Usas el esquema del planificador para escribir el contenido.",
            allow_delegation=False,
            llm=model,
            verbose=True
        )

        editor = Agent(
            role="🧐 Editor",
            goal="Revisar y pulir el artículo final.",
            backstory="Corriges errores, mejoras la redacción y verificas la coherencia.",
            allow_delegation=False,
            llm=model,
            verbose=True
        )

        # Definir tareas
        plan = Task(
            description=(
                f"📌 Analiza el tema **{topic}** relacionado con videojuegos y obtén noticias relevantes.\n"
                "📌 Define los puntos clave y estructura el artículo."
            ),
            expected_output="📜 Un plan de contenido detallado con estructura y palabras clave.",
            agent=planner,
        )

        write = Task(
            description=(
                f"📌 Usa el plan generado para escribir un artículo sobre videojuegos: **{topic}**.\n"
                "📌 Asegura un tono atractivo y una estructura clara."
            ),
            expected_output="📖 Un artículo bien estructurado con introducción, cuerpo y conclusión.",
            agent=writer,
        )

        edit = Task(
            description=(
                f"📌 Revisa el artículo generado sobre videojuegos: **{topic}**.\n"
                "📌 Corrige errores gramaticales y mejora la claridad del texto."
            ),
            expected_output="✅ Un artículo final pulido y listo para publicación.",
            agent=editor,
        )

        # Crear el equipo
        crew = Crew(
            agents=[planner, writer, editor],
            tasks=[plan, write, edit],
            verbose=True
        )

        # Ejecución de la tarea
        st.subheader("🚀 Progreso en tiempo real")

        # Apartados para cada agente
        planner_container = st.empty()
        writer_container = st.empty()
        editor_container = st.empty()
        final_container = st.empty()

        # Ejecutar CrewAI con seguimiento en tiempo real
        for task, agent, container in zip([plan, write, edit], [planner, writer, editor],
                                          [planner_container, writer_container, editor_container]):
            container.markdown(f"### {agent.role}\n⌛ **Procesando...**")
            result = crew.kickoff(inputs={"topic": topic})  # Ejecuta la tarea
            container.markdown(f"### {agent.role}\n✅ **Completado:**\n\n{result}")

        # Mostrar el resultado final
        final_container.subheader("📝 Artículo Final")
        final_container.markdown(result, unsafe_allow_html=True)