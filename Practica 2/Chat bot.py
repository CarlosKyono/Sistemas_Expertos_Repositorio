# chat_sencillo_tkinter.py
import tkinter as tk
from tkinter import scrolledtext

# --- Base de conocimiento inicial ---
base_conocimiento = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Estoy bien, gracias por preguntar. ¿Y tú?",
    "de que te gustaria hablar": "Podemos hablar de tecnología, música o películas. ¿Cuál prefieres?"
}

def buscar_respuesta(pregunta):
    """Busca la respuesta en la base de conocimiento."""
    return base_conocimiento.get(pregunta.lower().strip(), None)

def enviar_mensaje(event=None):
    entrada = entrada_usuario.get().strip()
    if not entrada:
        return

    mostrar_texto(f"Tú: {entrada}\n")
    entrada_usuario.delete(0, tk.END)

    if entrada.lower() == "salir":
        mostrar_texto("🤖 ChatBot: ¡Hasta luego!\n")
        ventana.after(1500, ventana.destroy)
        return

    respuesta = buscar_respuesta(entrada)
    if respuesta:
        mostrar_texto(f"🤖 ChatBot: {respuesta}\n")
    else:
        mostrar_texto("🤖 ChatBot: No sé cómo responder eso.\n")
        respuesta_nueva = preguntar_respuesta(entrada)
        if respuesta_nueva:
            base_conocimiento[entrada.lower()] = respuesta_nueva
            mostrar_texto("🤖 ChatBot: ¡Gracias! He aprendido algo nuevo.\n")
        else:
            mostrar_texto("🤖 ChatBot: Entendido, no lo guardaré.\n")

def mostrar_texto(texto):
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, texto)
    chat_area.yview(tk.END)
    chat_area.config(state=tk.DISABLED)

def preguntar_respuesta(pregunta):
    """Abre una ventana emergente para que el usuario enseñe algo nuevo."""
    ventana_respuesta = tk.Toplevel(ventana)
    ventana_respuesta.title("Enseñar al ChatBot")
    tk.Label(ventana_respuesta, text=f"¿Cuál sería una buena respuesta para:\n'{pregunta}'?").pack(padx=10, pady=10)

    entrada_respuesta = tk.Entry(ventana_respuesta, width=50)
    entrada_respuesta.pack(pady=5)

    respuesta = {"valor": None}

    def guardar():
        valor = entrada_respuesta.get().strip()
        if valor.lower() != "ninguna" and valor:
            respuesta["valor"] = valor
        ventana_respuesta.destroy()

    tk.Button(ventana_respuesta, text="Guardar", command=guardar).pack(pady=5)
    ventana_respuesta.grab_set()
    ventana_respuesta.wait_window()
    return respuesta["valor"]

# --- Configuración de la ventana principal ---
ventana = tk.Tk()
ventana.title("ChatBot Sencillo")

chat_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
chat_area.pack(padx=10, pady=10)

entrada_usuario = tk.Entry(ventana, width=50)
entrada_usuario.pack(side=tk.LEFT, padx=10, pady=5, expand=True, fill=tk.X)
entrada_usuario.bind("<Return>", enviar_mensaje)

boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(side=tk.RIGHT, padx=10, pady=5)

mostrar_texto("🤖 ChatBot: ¡Hola! Soy tu asistente. Escribe algo o 'salir' para terminar.\n")

ventana.mainloop()
