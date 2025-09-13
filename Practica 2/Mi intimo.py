# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# --- Base de conocimiento inicial ---
base_conocimiento = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Estoy bien, gracias por preguntar. ¿Y tú?",
    "de que te gustaria hablar": "Podemos hablar de tecnología, música o películas. ¿Cuál prefieres?"
}

def buscar_respuesta(pregunta):
    """Busca la respuesta en la base de conocimiento."""
    pregunta = pregunta.lower().strip()
    return base_conocimiento.get(pregunta, None)

def chat():
    print("🤖 ChatBot sencillo")
    print("Escribe 'salir' para terminar.\n")

    while True:
        entrada = input("Tú: ").lower().strip()

        if entrada == "salir":
            print("🤖 ChatBot: ¡Hasta luego!")
            break

        respuesta = buscar_respuesta(entrada)

        if respuesta:
            print(f"🤖 ChatBot: {respuesta}")
        else:
            print("🤖 ChatBot: No sé cómo responder eso.")
            nueva_respuesta = input("¿Cuál sería una buena respuesta para esta pregunta? (o escribe 'ninguna' si no quieres enseñar): ").strip()

            if nueva_respuesta.lower() != "ninguna":
                base_conocimiento[entrada] = nueva_respuesta
                print("🤖 ChatBot: ¡Gracias! He aprendido algo nuevo.")
            else:
                print("🤖 ChatBot: Entendido, no lo guardaré.")

if __name__ == "__main__":
    chat()

