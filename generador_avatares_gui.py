import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk
import re
import python_avatars as pa
from generador_avatares import (
    colores_piel, colores_cabello, tipos_cabello, tipos_barba,
    colores_ropa, tipos_ropa, accesorios as tipos_accesorios,
    tipos_nariz, tipos_cejas, tipos_ojos, tipos_boca,
    colores_sombrero, graficos_camiseta, patrones
)

# Diccionario de estilos de avatar agregado para corregir el import
estilos_avatar = {
    "círculo": pa.AvatarStyle.CIRCLE,
    "transparente": pa.AvatarStyle.TRANSPARENT
}

img_tk = None

def generar_avatar(descripcion):
    bloques = re.findall(r"\(.*?\)", descripcion.lower())

    # Defaults
    skin = pa.SkinColor.LIGHT
    hair_color = pa.HairColor.BROWN
    top_type = pa.TopType.SHORT_HAIR_SHORT_FLAT
    facial_hair = pa.FacialHairType.DEFAULT
    clothe_color = pa.Color.BLACK
    clothe_type = pa.ClotheType.GRAPHIC_SHIRT
    accessories = pa.AccessoriesType.DEFAULT
    nose_type = pa.NoseType.DEFAULT
    eyebrow_type = pa.EyebrowType.DEFAULT
    eye_type = pa.EyesType.DEFAULT
    mouth_type = pa.MouthType.DEFAULT
    hat_color = pa.Color.BLACK
    graphic_type = pa.ClotheGraphicType.BAT
    avatar_style = pa.AvatarStyle.CIRCLE

    errores = []

    for bloque in bloques:
        if match := patrones["cabello"].fullmatch(bloque):
            color = match.group("color")
            tipo = match.group("tipo")
            hair_color = colores_cabello.get(color, hair_color)
            if tipo:
                top_type = tipos_cabello.get(tipo, top_type)
        elif match := patrones["piel"].fullmatch(bloque):
            color = match.group("color")
            skin = colores_piel.get(color, skin)
        elif match := patrones["barba"].fullmatch(bloque):
            tipo = match.group("tipo")
            facial_hair = tipos_barba.get(tipo, facial_hair)
        elif match := patrones["ropa"].fullmatch(bloque):
            color = match.group("color")
            clothe_color = colores_ropa.get(color, clothe_color)
        elif match := patrones["tipo_ropa"].fullmatch(bloque):
            tipo = match.group("tipo")
            clothe_type = tipos_ropa.get(tipo, clothe_type)
        elif match := patrones["accesorios"].fullmatch(bloque):
            tipo = match.group("tipo")
            accessories = tipos_accesorios.get(tipo, accessories)
        elif match := patrones["nariz"].fullmatch(bloque):
            tipo = match.group("tipo")
            nose_type = tipos_nariz.get(tipo, nose_type)
        elif match := patrones["cejas"].fullmatch(bloque):
            tipo = match.group("tipo")
            eyebrow_type = tipos_cejas.get(tipo, eyebrow_type)
        elif match := patrones["ojos"].fullmatch(bloque):
            tipo = match.group("tipo")
            eye_type = tipos_ojos.get(tipo, eye_type)
        elif match := patrones["boca"].fullmatch(bloque):
            tipo = match.group("tipo")
            mouth_type = tipos_boca.get(tipo, mouth_type)
        elif match := patrones["sombrero"].fullmatch(bloque):
            color = match.group("color")
            hat_color = colores_sombrero.get(color, hat_color)
        elif match := patrones["grafico"].fullmatch(bloque):
            tipo = match.group("tipo")
            graphic_type = graficos_camiseta.get(tipo, graphic_type)
        elif match := patrones["estilo"].fullmatch(bloque):
            tipo = match.group("tipo")
            avatar_style = estilos_avatar.get(tipo, avatar_style)
        else:
            errores.append(f"Bloque no reconocido: {bloque}")

    if errores:
        return None, errores

    avatar = pa.PyAvataaar(
        style=avatar_style,
        skin_color=skin,
        hair_color=hair_color,
        top_type=top_type,
        facial_hair_type=facial_hair,
        facial_hair_color=hair_color,
        clothe_color=clothe_color,
        clothe_type=clothe_type,
        accessories_type=accessories,
        nose_type=nose_type,
        eyebrow_type=eyebrow_type,
        eye_type=eye_type,
        mouth_type=mouth_type,
        hat_color=hat_color,
        clothe_graphic_type=graphic_type
    )
    avatar.render_png_file("avatar_gui.png")
    return "avatar_gui.png", None

def mostrar_opciones_ventana():
    ventana = Toplevel()
    ventana.title("Opciones Disponibles")
    ventana.geometry("750x600")
    texto = tk.Text(ventana, wrap="word", font=("Courier New", 10))
    texto.insert("1.0", """
🎨 OPCIONES DISPONIBLES

✔️ Estilo
(estilo círculo), (estilo transparente)

✔️ Color de Piel
(piel negra), (piel clara), (piel amarilla), etc.

✔️ Cabello
(cabello color negro calvo), (cabello color rojo rizado)

✔️ Barba
(barba larga), (barba media), (bigote), (sin barba)

✔️ Ropa
(ropa blanca), (ropa gris), etc.
(tipo de ropa camiseta), (tipo de ropa hoodie)

✔️ Accesorios
(accesorio gafas redondas), (accesorio gafas sol)

✔️ Nariz
(nariz default)

✔️ Cejas
(cejas normales), (cejas enojadas), (cejas tristes)

✔️ Ojos
(ojos feliz), (ojos corazón), (ojos cerrados)

✔️ Boca
(boca sonrisa), (boca abierta), (boca triste)

✔️ Sombrero
(sombrero color rojo), (sombrero color blanco)

✔️ Camiseta Gráfica
(grafico pizza), (grafico calavera), (grafico hola)
    """)
    texto.pack(expand=True, fill="both")
    texto.configure(state="disabled")


def lanzar_gui():
    global entrada, label_imagen, img_tk

    root = tk.Tk()
    root.title("Generador de Avatares con Paréntesis")
    root.geometry("700x620")

    tk.Label(root, text="✏️ Escribe la descripción del avatar:", font=("Arial", 14)).pack(pady=10)
    entrada = tk.Text(root, height=4, font=("Arial", 12))
    entrada.pack(pady=10)

    label_imagen = tk.Label(root)
    label_imagen.pack(pady=10)

    def previsualizar():
        global img_tk
        texto = entrada.get("1.0", "end").strip()
        path_imagen, errores = generar_avatar(texto)
        if errores:
            messagebox.showerror("Errores encontrados", "\n".join(errores))
        elif path_imagen:
            imagen = Image.open(path_imagen)
            imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(imagen)
            label_imagen.config(image=img_tk)
            label_imagen.image = img_tk
        else:
            messagebox.showwarning("Oops", "No se pudo generar el avatar.")

    tk.Button(root, text="🎨 Generar Avatar", command=previsualizar, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=5)
    tk.Button(root, text="📋 Ver Opciones", command=mostrar_opciones_ventana, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    lanzar_gui()