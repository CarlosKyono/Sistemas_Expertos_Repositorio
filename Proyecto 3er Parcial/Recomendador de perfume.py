import sqlite3
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# ===============================
# CREAR BASE DE DATOS
# ===============================
def crear_bd():
    conn = sqlite3.connect("perfumes.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS perfumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            aroma TEXT,
            intensidad TEXT,
            estilo TEXT,
            ocasion TEXT,
            precio INTEGER
        )
    """)

    # Tabla historial
    c.execute("""
        CREATE TABLE IF NOT EXISTS historial (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            aroma TEXT,
            intensidad TEXT,
            estilo TEXT,
            ocasion TEXT,
            presupuesto INTEGER
        )
    """)

    if c.execute("SELECT COUNT(*) FROM perfumes").fetchone()[0] == 0:
        # ======== PEGA AQUÍ TU BASE DE DATOS DE PERFUMES ========
        
        perfumes = [
                ("Dior Sauvage","Amaderado","Alta","Formal","Noche",120),
                ("Bleu de Chanel","Cítrico","Media","Elegante","Trabajo",135),
                ("Versace Eros","Dulce","Alta","Juvenil","Fiesta",95),
                ("Acqua di Gio Profumo","Acuático","Media","Casual","Diario",110),
                ("Paco Rabanne 1 Million","Especiado","Alta","Juvenil","Fiesta",100),
                ("Hugo Boss Bottled","Frutal","Media","Elegante","Trabajo",85),
                ("Armani Code","Oriental","Alta","Formal","Noche",125),
                ("YSL Y EDP","Aromático","Media","Moderno","Diario",115),
                ("Dolce & Gabbana The One","Amaderado","Alta","Elegante","Cita",130),
                ("Jean Paul Gaultier Le Male","Dulce","Media","Clásico","Fiesta",105),
            
                ("Tom Ford Noir","Oriental","Alta","Formal","Evento",150),
                ("Montblanc Explorer","Amaderado","Media","Casual","Aventura",90),
                ("Givenchy Gentleman","Amaderado","Alta","Formal","Trabajo",140),
                ("Creed Aventus","Frutal","Alta","Lujo","Evento",300),
                ("Bentley Intense","Especiado","Alta","Formal","Noche",95),
                ("Lattafa Asad","Especiado","Alta","Moderno","Fiesta",60),
                ("Rasasi Hawas","Aromático","Media","Juvenil","Verano",75),
                ("Afnan 9PM","Dulce","Alta","Juvenil","Noche",50),
                ("Viktor & Rolf Spicebomb","Especiado","Alta","Moderno","Invierno",120),
                ("Burberry Hero","Amaderado","Media","Elegante","Trabajo",110),
            
                ("Carolina Herrera Bad Boy","Oriental","Alta","Moderno","Noche",115),
                ("Issey Miyake L’Eau d’Issey","Cítrico","Media","Clásico","Verano",95),
                ("Club de Nuit Intense Man","Amaderado","Alta","Moderno","Diario",70),
                ("Mancera Cedrat Boise","Cítrico","Alta","Lujo","Evento",140),
                ("Invictus Victory","Dulce","Alta","Juvenil","Fiesta",105),
                ("Dolce & Gabbana Light Blue Homme","Cítrico","Media","Casual","Verano",85),
                ("CK One","Cítrico","Baja","Casual","Diario",55),
                ("Eros Flame","Especiado","Alta","Juvenil","Fiesta",110),
                ("Fahrenheit","Oriental","Alta","Clásico","Noche",100),
                ("212 VIP Men","Oriental","Alta","Moderno","Fiesta",120),
            
                ("Bvlgari Man in Black","Oriental","Alta","Formal","Noche",135),
                ("Prada Luna Rossa Carbon","Amaderado","Media","Moderno","Diario",115),
                ("Valentino Uomo","Amaderado","Alta","Elegante","Cita",145),
                ("Boss The Scent","Oriental","Media","Elegante","Cita",110),
                ("Azzaro Wanted","Aromático","Media","Juvenil","Fiesta",95),
                ("Nautica Voyage","Acuático","Media","Casual","Diario",40),
                ("Abercrombie & Fitch Fierce","Amaderado","Media","Juvenil","Diario",90),
                ("Lacoste Blanc","Cítrico","Media","Casual","Diario",95),
                ("Diesel Only The Brave","Oriental","Alta","Juvenil","Fiesta",85),
                ("John Varvatos Artisan","Cítrico","Media","Casual","Diario",75),
            
                ("Maison Francis Kurkdjian Baccarat Rouge 540","Oriental","Alta","Lujo","Evento",320),
                ("Parfums de Marly Layton","Amaderado","Alta","Lujo","Evento",280),
                ("Xerjoff Naxos","Oriental","Alta","Lujo","Evento",350),
                ("Amouage Interlude Man","Amaderado","Alta","Lujo","Evento",360),
                ("Emporio Armani Stronger With You","Dulce","Alta","Moderno","Cita",125),
                ("Paco Rabanne Phantom","Aromático","Media","Moderno","Fiesta",115),
                ("Yves Saint Laurent Y Le Parfum","Aromático","Alta","Moderno","Noche",140),
                ("Jean Paul Gaultier Ultra Male","Dulce","Alta","Juvenil","Fiesta",120),
                ("Salvatore Ferragamo Uomo","Oriental","Alta","Elegante","Cita",100),
                ("Ralph Lauren Polo Blue","Acuático","Media","Clásico","Trabajo",95),
            
                ("Ralph Lauren Polo Red","Especiado","Alta","Moderno","Fiesta",105),
                ("Dunhill Icon","Amaderado","Media","Elegante","Trabajo",150),
                ("Kenzo Homme","Acuático","Media","Casual","Verano",90),
                ("Calvin Klein Eternity","Aromático","Media","Clásico","Trabajo",85),
                ("Thierry Mugler A*Men","Oriental","Alta","Clásico","Noche",95),
                ("Hermès Terre d’Hermès","Amaderado","Media","Elegante","Trabajo",130),
                ("Initio Oud for Greatness","Oriental","Alta","Lujo","Evento",380),
                ("Byredo Gypsy Water","Amaderado","Media","Lujo","Diario",250)
]
        c.executemany("INSERT INTO perfumes VALUES (NULL,?,?,?,?,?,?)", perfumes)

    conn.commit()
    conn.close()

# ===============================
# VARIABLES GLOBALES
# ===============================
lista_resultados = []
indice_actual = 0

# ===============================
# MOTOR DE INFERENCIA
# ===============================
def inferir():
    global lista_resultados, indice_actual

    try:
        aroma = aroma_var.get()
        intensidad = intensidad_var.get()
        estilo = estilo_var.get()
        ocasion = ocasion_var.get()
        presupuesto = int(presupuesto_var.get())
    except:
        resultado_label.config(text="Por favor ingresa un presupuesto válido.")
        return

    conn = sqlite3.connect("perfumes.db")
    c = conn.cursor()

    # Guardar historial
    c.execute("""
        INSERT INTO historial (fecha, aroma, intensidad, estilo, ocasion, presupuesto)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          aroma, intensidad, estilo, ocasion, presupuesto))

    querys = [
        ("SELECT nombre, precio, aroma, intensidad, estilo, ocasion FROM perfumes WHERE aroma=? AND intensidad=? AND estilo=? AND ocasion=? AND precio<=? LIMIT 5",
         (aroma, intensidad, estilo, ocasion, presupuesto)),

        ("SELECT nombre, precio, aroma, intensidad, estilo, ocasion FROM perfumes WHERE aroma=? AND intensidad=? AND ocasion=? AND precio<=? LIMIT 5",
         (aroma, intensidad, ocasion, presupuesto)),

        ("SELECT nombre, precio, aroma, intensidad, estilo, ocasion FROM perfumes WHERE aroma=? AND intensidad=? AND precio<=? LIMIT 5",
         (aroma, intensidad, presupuesto)),

        ("SELECT nombre, precio, aroma, intensidad, estilo, ocasion FROM perfumes WHERE aroma=? AND precio<=? LIMIT 5",
         (aroma, presupuesto))
    ]

    resultados = []
    for q, p in querys:
        c.execute(q, p)
        resultados = c.fetchall()
        if resultados:
            break

    if not resultados:
        c.execute("""
            SELECT nombre, precio, aroma, intensidad, estilo, ocasion
            FROM perfumes
            ORDER BY ABS(precio - ?) ASC
            LIMIT 5
        """, (presupuesto,))
        resultados = c.fetchall()

    conn.commit()
    conn.close()

    # Guardar resultados y resetear índice
    lista_resultados = resultados
    indice_actual = 0

    if lista_resultados:
        mostrar_recomendacion()
    else:
        resultado_label.config(text="No se encontraron recomendaciones.")

# ===============================
# MOSTRAR UNA A LA VEZ
# ===============================
def mostrar_recomendacion():
    global indice_actual

    if not lista_resultados:
        return

    if indice_actual >= len(lista_resultados):
        resultado_label.config(text="No hay más recomendaciones.")
        return

    n, p, a, inten, est, oc = lista_resultados[indice_actual]

    # Calcular compatibilidad
    total = 5
    puntos = 0
    if a == aroma_var.get(): puntos += 1
    if inten == intensidad_var.get(): puntos += 1
    if est == estilo_var.get(): puntos += 1
    if oc == ocasion_var.get(): puntos += 1
    if p <= int(presupuesto_var.get()): puntos += 1

    match = int((puntos / total) * 100)

    # Construir razones
    razones = []
    if a == aroma_var.get(): razones.append(f"aroma {a}")
    if inten == intensidad_var.get(): razones.append(f"intensidad {inten}")
    if est == estilo_var.get(): razones.append(f"estilo {est}")
    if oc == ocasion_var.get(): razones.append(f"ocasión {oc}")
    if p <= int(presupuesto_var.get()): razones.append("dentro del presupuesto")

    texto = " TOP 4 RECOMENDACIONES\n\n"
    texto += f"Recomendación {indice_actual + 1} de {len(lista_resultados)}\n\n"
    texto += f"{n} - ${p} USD\n"
    texto += f"Compatibilidad: {match}%\n"
    texto += f"Motivo: coincide en {', '.join(razones)}"

    resultado_label.config(text=texto)

def siguiente_recomendacion():
    global indice_actual
    indice_actual += 1
    mostrar_recomendacion()

# ===============================
# UI
# ===============================
crear_bd()

ventana = tk.Tk()
ventana.title("Sistema Experto de Perfumes")
ventana.geometry("650x650")
FONDO = "#0f172a"
ventana.configure(bg=FONDO)

# Bienvenida
pantalla_bienvenida = tk.Frame(ventana, bg=FONDO)
pantalla_bienvenida.pack(fill="both", expand=True)

tk.Label(
    pantalla_bienvenida,
    text=" Bienvenido al Sistema Experto de Fragancias Masculinas ",
    fg="#e5e7eb",
    bg=FONDO,
    font=("Times New Roman", 22, "bold")
).pack(pady=120)

tk.Label(
    pantalla_bienvenida,
    text="Encuentra tu aroma ideal paso a paso",
    fg="#cbd5f5",
    bg=FONDO,
    font=("Arial", 14, "italic")
).pack(pady=10)

tk.Button(
    pantalla_bienvenida,
    text="Entrar al recomendador",
    font=("Arial", 14, "bold"),
    bg="#334155",
    fg="white",
    command=lambda: (pantalla_bienvenida.pack_forget(), pantalla_principal.pack(fill="both", expand=True))
).pack(pady=40)

# Pantalla principal
pantalla_principal = tk.Frame(ventana, bg=FONDO)

def crear_label(txt):
    return tk.Label(pantalla_principal, text=txt, fg="white", bg=FONDO, font=("Arial", 12))

crear_label("¿Qué tipo de aroma prefieres?").pack()
aroma_var = tk.StringVar()
ttk.Combobox(pantalla_principal, textvariable=aroma_var,
    values=["Amaderado","Cítrico","Dulce","Acuático","Especiado","Frutal","Oriental","Aromático"],
    state="readonly").pack()

crear_label("¿Qué intensidad prefieres?").pack()
intensidad_var = tk.StringVar()
ttk.Combobox(pantalla_principal, textvariable=intensidad_var,
    values=["Alta","Media","Baja"],
    state="readonly").pack()

crear_label("¿Qué estilo buscas?").pack()
estilo_var = tk.StringVar()
ttk.Combobox(pantalla_principal, textvariable=estilo_var,
    values=["Formal","Casual","Elegante","Juvenil","Moderno","Clásico","Lujo"],
    state="readonly").pack()

crear_label("¿Para qué ocasión lo necesitas?").pack()
ocasion_var = tk.StringVar()
ttk.Combobox(pantalla_principal, textvariable=ocasion_var,
    values=["Fiesta","Trabajo","Diario","Evento","Cita","Noche","Aventura","Verano","Invierno"],
    state="readonly").pack()

crear_label("Presupuesto máximo (USD)").pack()
presupuesto_var = tk.StringVar()
tk.Entry(pantalla_principal, textvariable=presupuesto_var).pack()

tk.Button(pantalla_principal, text="Recomendar", command=inferir).pack(pady=10)

tk.Button(pantalla_principal, text="Siguiente recomendación", command=siguiente_recomendacion).pack(pady=5)

tk.Button(pantalla_principal, text="Nueva recomendación", command=lambda: [
    aroma_var.set(""), intensidad_var.set(""), estilo_var.set(""),
    ocasion_var.set(""), presupuesto_var.set(""), resultado_label.config(text="")
]).pack()

tk.Button(pantalla_principal, text="Cerrar", command=ventana.destroy).pack(pady=10)

resultado_label = tk.Label(pantalla_principal, text="", fg="white", bg=FONDO, wraplength=550, justify="center")
resultado_label.pack(pady=10)

ventana.mainloop()
