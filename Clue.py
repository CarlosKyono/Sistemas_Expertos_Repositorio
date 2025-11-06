import tkinter as tk
from tkinter import messagebox
import random

# --- Datos base ---
personajes = [
    {"name": "Lucía Navarro", "profession": "Historiadora"},
    {"name": "Martín Gutiérrez", "profession": "Ingeniero"},
    {"name": "Sofía Rojas", "profession": "Chef"},
    {"name": "Héctor Salinas", "profession": "Anticuario"},
    {"name": "Valeria Paredes", "profession": "Abogada"},
]

armas = ["Candelabro", "Cuchillo", "Revólver", "Cuerda", "Tubo de plomo"]
locaciones = ["Biblioteca", "Cocina", "Estudio", "Invernadero", "Salón de música"]

# --- Selección aleatoria ---
culpable = random.choice(personajes)
arma = random.choice(armas)
lugar = random.choice(locaciones)
intentos = 3

# --- Historia de introducción ---
historia_intro = (
    "La lluvia cae sin descanso sobre la vieja mansión de los Navarro. "
    "El trueno ruge, las luces parpadean… y de pronto, un grito atraviesa la oscuridad.\n\n"
    "Cinco invitados se habían reunido esa noche para hablar sobre un antiguo testamento. "
    "Pero antes de la medianoche, uno de ellos no volvería a ver el amanecer.\n\n"
    "Tu misión es descubrir quién cometió el crimen, con qué arma y en qué lugar.\n"
    "Observa bien, cada detalle importa."
)

# --- Función para verificar respuesta ---
def verificar():
    global intentos
    nombre = entry_nombre.get().strip().lower()
    arma_guess = entry_arma.get().strip().lower()
    lugar_guess = entry_lugar.get().strip().lower()

    correcto_nombre = any(nombre in parte.lower() for parte in culpable["name"].split())
    correcto_arma = arma_guess == arma.lower()
    correcto_lugar = lugar_guess == lugar.lower()

    if correcto_nombre and correcto_arma and correcto_lugar:
        mostrar_historia(True)
    else:
        intentos -= 1
        if intentos > 0:
            lbl_resultado.config(text=f"❌ Fallaste. Intentos restantes: {intentos}")
        else:
            lbl_resultado.config(text="☠️ Has agotado tus intentos...")
            mostrar_historia(False)

# --- Función para mostrar el resultado ---
def mostrar_historia(acierto):
    if acierto:
        historia = (
            f"🔎 ¡Correcto! El culpable fue {culpable['name']}, {culpable['profession']}.\n\n"
            f"Usó el {arma} en el {lugar}.\n\n"
            "Mientras la tormenta rugía afuera, nadie escuchó el golpe. "
            "El asesino planeó todo cuidadosamente: sabía cuándo las luces parpadearían "
            "y cuándo el grito se perdería entre los truenos.\n\n"
            "Cuando la policía llegó, el silencio era absoluto… solo el reloj marcaba las doce."
        )
        messagebox.showinfo("Caso resuelto", historia)
    else:
        historia = (
            f"El culpable era {culpable['name']} ({culpable['profession']}).\n"
            f"El crimen ocurrió en el {lugar}, con el {arma}.\n\n"
            "La verdad salió a la luz con el amanecer. El culpable, acorralado por las pistas, "
            "no pudo sostener más la mentira.\n\n"
            "Entre los ecos de la tormenta, la mansión vuelve a quedar en silencio..."
        )
        messagebox.showerror("Misterio revelado", historia)
    root.destroy()

# --- Interfaz Tkinter ---
root = tk.Tk()
root.title("🕯️ Clue: Misterio en la Mansión")
root.geometry("700x600")
root.config(bg="#111")

# --- Título ---
lbl_title = tk.Label(
    root, text="Clue: Misterio en la Mansión",
    font=("Courier", 22, "bold"), fg="#ffcc66", bg="#111"
)
lbl_title.pack(pady=15)

# --- Historia introductoria ---
lbl_intro = tk.Label(
    root, text=historia_intro, wraplength=650, justify="left",
    font=("Courier", 11), fg="#ccc", bg="#111"
)
lbl_intro.pack(pady=10)

# --- Lista de personajes ---
lista_personajes = "\n".join([f"- {p['name']} ({p['profession']})" for p in personajes])
lbl_personajes = tk.Label(
    root, text=f"Posibles sospechosos:\n{lista_personajes}",
    font=("Courier", 10), fg="#ffcc66", bg="#111", justify="left"
)
lbl_personajes.pack(pady=10)

# --- Entradas ---
frame_inputs = tk.Frame(root, bg="#111")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Sospechoso:", font=("Courier", 12), fg="#ffcc66", bg="#111").grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(frame_inputs, font=("Courier", 12), width=25, bg="#222", fg="#fff", insertbackground="#fff")
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Arma:", font=("Courier", 12), fg="#ffcc66", bg="#111").grid(row=1, column=0, sticky="e")
entry_arma = tk.Entry(frame_inputs, font=("Courier", 12), width=25, bg="#222", fg="#fff", insertbackground="#fff")
entry_arma.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Locación:", font=("Courier", 12), fg="#ffcc66", bg="#111").grid(row=2, column=0, sticky="e")
entry_lugar = tk.Entry(frame_inputs, font=("Courier", 12), width=25, bg="#222", fg="#fff", insertbackground="#fff")
entry_lugar.grid(row=2, column=1, padx=10, pady=5)

# --- Botón de verificación ---
btn_verificar = tk.Button(
    root, text="Verificar respuesta", font=("Courier", 12, "bold"),
    bg="#ffcc66", fg="#000", width=25, command=verificar
)
btn_verificar.pack(pady=20)

# --- Resultado ---
lbl_resultado = tk.Label(root, text="", font=("Courier", 12), fg="#ff6666", bg="#111")
lbl_resultado.pack()

# --- Instrucciones visuales ---
lbl_datos = tk.Label(
    root, text=f"\nArmas disponibles:\n{', '.join(armas)}\n\nLugares:\n{', '.join(locaciones)}",
    font=("Courier", 10), fg="#888", bg="#111", justify="left"
)
lbl_datos.pack(pady=10)

# --- Iniciar interfaz ---
root.mainloop()
