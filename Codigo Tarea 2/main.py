import os
import cv2
from deepface import DeepFace

# ---------- RUTAS ----------
img_path = "C:/Users/ketze/Desktop/3 Parcial/DeepFace/FACES/ANA D ARMAS.jpg"
db_path = "C:/Users/ketze/Desktop/3 Parcial/DeepFace/known_faces"

# ---------- CARGAR IMAGEN ----------
img = cv2.imread(img_path)
if img is None:
    print("❌ No se pudo cargar la imagen. Verifica la ruta:")
    print(img_path)
    exit()

# ---------- ANALIZAR EMOCIÓN, EDAD Y GÉNERO ----------
print("🔍 Analizando rostro...")
results = DeepFace.analyze(img, actions=["age", "gender", "emotion"], enforce_detection=False)
age = results[0]["age"]
gender = results[0]["gender"]
dominant_emotion = results[0]["dominant_emotion"]

# ---------- IDENTIFICACIÓN FACIAL ----------
print("🔎 Buscando identidad en la base de datos...")
identified_name = "Desconocida"
try:
    df = DeepFace.find(img_path=img_path, db_path=db_path, enforce_detection=False)
    if len(df[0]) > 0:
        identity_path = df[0].iloc[0]['identity']
        identified_name = os.path.splitext(os.path.basename(identity_path))[0]
        print(f"🎭 Actriz identificada: {identified_name}")
    else:
        print("⚠️ No se encontró coincidencia en la base de datos.")
except Exception as e:
    print("❌ Error en identificación:", str(e))

# ---------- MOSTRAR IMAGEN CON INFORMACIÓN ----------
output_text = f"Nombre: {identified_name}\nEdad: {int(age)}\nGénero: {gender}\nEmoción: {dominant_emotion}"

# Dibujar texto sobre la imagen
y0, dy = 30, 30
for i, line in enumerate(output_text.split('\n')):
    y = y0 + i * dy
    cv2.putText(img, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Mostrar la imagen
cv2.imshow("Resultado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
