import json
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

DATA_FILE = "pokemon_akinator.json"

# Cargar o inicializar base de conocimiento
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        # Base inicial con más Pokémon
        base_inicial = {
            "question": "¿Es de tipo fuego?",
            "yes": {
                "question": "¿Tiene forma de reptil?",
                "yes": {"pokemon": "Charmander"},
                "no": {"pokemon": "Vulpix"}
            },
            "no": {
                "question": "¿Es de tipo agua?",
                "yes": {
                    "question": "¿Tiene concha?",
                    "yes": {"pokemon": "Squirtle"},
                    "no": {"pokemon": "Psyduck"}
                },
                "no": {
                    "question": "¿Es de tipo planta?",
                    "yes": {
                        "question": "¿Tiene un bulbo o flor en el cuerpo?",
                        "yes": {"pokemon": "Bulbasaur"},
                        "no": {"pokemon": "Oddish"}
                    },
                    "no": {
                        "question": "¿Es de tipo eléctrico?",
                        "yes": {
                            "question": "¿Es pequeño y de color amarillo?",
                            "yes": {"pokemon": "Pikachu"},
                            "no": {"pokemon": "Magnemite"}
                        },
                        "no": {
                            "question": "¿Es de tipo volador?",
                            "yes": {
                                "question": "¿Tiene cuerpo de ave?",
                                "yes": {"pokemon": "Pidgey"},
                                "no": {"pokemon": "Zubat"}
                            },
                            "no": {
                                "question": "¿Es de tipo normal?",
                                "yes": {
                                    "question": "¿Parece un pequeño zorro?",
                                    "yes": {"pokemon": "Eevee"},
                                    "no": {"pokemon": "Jigglypuff"}
                                },
                                "no": {"pokemon": "Mewtwo"}
                            }
                        }
                    }
                }
            }
        }
        save_data(base_inicial)
        return base_inicial

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

class AkinatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Akinator de Pokémon (1ra generación)")
        self.master.geometry("600x400")
        self.master.config(bg="#f4f4f4")

        self.knowledge = load_data()
        self.current_node = self.knowledge
        self.path = []  # Guarda las decisiones (sí/no)

        self.label = tk.Label(
            master,
            text=" Bienvenido al Akinator de Pokémon \n\nPiensa en un Pokémon de la primera generación.",
            font=("Arial", 14),
            bg="#f4f4f4",
            wraplength=500,
            justify="center"
        )
        self.label.pack(pady=40)

        self.button_frame = tk.Frame(master, bg="#f4f4f4")
        self.button_frame.pack(pady=20)

        self.yes_button = tk.Button(
            self.button_frame,
            text="Sí",
            width=15,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            command=lambda: self.answer("yes")
        )
        self.yes_button.grid(row=0, column=0, padx=20)

        self.no_button = tk.Button(
            self.button_frame,
            text="No",
            width=15,
            height=2,
            bg="#F44336",
            fg="white",
            font=("Arial", 12, "bold"),
            command=lambda: self.answer("no")
        )
        self.no_button.grid(row=0, column=1, padx=20)

        self.start_game()

    def start_game(self):
        self.current_node = self.knowledge
        self.path = []
        self.update_label()

    def update_label(self):
        if "pokemon" in self.current_node:
            self.label.config(text=f"¿Es tu Pokémon {self.current_node['pokemon']}?")
        else:
            self.label.config(text=self.current_node["question"])

    def answer(self, choice):
        if "pokemon" in self.current_node:
            if choice == "yes":
                messagebox.showinfo("¡Adivinado!", "¡Lo adiviné! ")
                self.play_again()
            else:
                self.learn()
        else:
            self.path.append((self.current_node, choice))
            self.current_node = self.current_node[choice]
            self.update_label()

    def learn(self):
        pokemon_usuario = simpledialog.askstring("Aprendiendo", "¿Cuál era tu Pokémon?")
        if not pokemon_usuario:
            messagebox.showinfo("Cancelado", "No se aprendió nada nuevo.")
            self.play_again()
            return

        nueva_pregunta = simpledialog.askstring(
            "Aprendiendo",
            f"Escribe una pregunta para diferenciar a {pokemon_usuario} de {self.current_node['pokemon']}:"
        )

        if not nueva_pregunta:
            messagebox.showinfo("Cancelado", "No se aprendió nada nuevo.")
            self.play_again()
            return

        respuesta_correcta = messagebox.askyesno(
            "Aprendiendo",
            f"Para {pokemon_usuario}, ¿la respuesta a esa pregunta sería 'Sí'?"
        )

        nuevo_nodo = {
            "question": nueva_pregunta,
            "yes": {"pokemon": pokemon_usuario} if respuesta_correcta else {"pokemon": self.current_node["pokemon"]},
            "no": {"pokemon": self.current_node["pokemon"]} if respuesta_correcta else {"pokemon": pokemon_usuario}
        }

        # Actualiza el nodo actual
        if self.path:
            parent, direction = self.path[-1]
            parent[direction] = nuevo_nodo
        else:
            self.knowledge = nuevo_nodo

        save_data(self.knowledge)
        messagebox.showinfo("Aprendido", "¡He aprendido un nuevo Pokémon! ")
        self.play_again()

    def play_again(self):
        again = messagebox.askyesno("Reinicio", "¿Quieres jugar otra vez?")
        if again:
            self.start_game()
        else:
            self.master.quit()

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AkinatorApp(root)
    root.mainloop()
