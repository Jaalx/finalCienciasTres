import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from lexicalProject import LexicalAnalyzer
from sintaticProject import SyntacticAnalyzer
from semanticProject import SemanticAnalyzer
import py_avataaars as pa

# Import all mapping dictionaries
from generador_avatares import (
    colores_cabello, tipos_cabello, colores_ropa, tipos_ropa, tipos_boca,
    tipos_ojos, tipos_cejas, accesorios as tipos_accesorios, colores_piel
)

class Compiler:
    def compile(self, code: str):
        try:
            # Compiler stages
            tokens = LexicalAnalyzer.lex(code)
            SyntacticAnalyzer(tokens).parse()

            try:
                avatar_config = SemanticAnalyzer(tokens).analyze()
            except ValueError as e:
                error_msg = f"[Semantic Error] {e}"
                if hasattr(e, 'line'):
                    error_msg = f"[Semantic Error] Line {e.line}: {e}"
                messagebox.showerror("Semantic Error", error_msg)
                return

            print("Avatar configuration:", avatar_config)
            output_path = "avatar_result.png"
            self.generate_avatar(avatar_config, output_path)
            self.show_avatar(output_path)

        except RuntimeError as e:
            messagebox.showerror("Lexical Error", str(e))
        except SyntaxError as e:
            messagebox.showerror("Syntactic Error", str(e))

    def generate_avatar(self, config: dict, output_path: str):
        avatar = pa.PyAvataaar(
            style=pa.AvatarStyle.CIRCLE,
            skin_color=colores_piel.get("clara", pa.SkinColor.LIGHT),
            hair_color=pa.HairColor.BROWN,
            top_type=pa.TopType.SHORT_HAIR_SHORT_FLAT,
            clothe_type=pa.ClotheType.GRAPHIC_SHIRT,
            clothe_color=pa.Color.BLACK,
            mouth_type=pa.MouthType.DEFAULT,
            eye_type=pa.EyesType.DEFAULT,
            eyebrow_type=pa.EyebrowType.DEFAULT,
            accessories_type=pa.AccessoriesType.DEFAULT,
        )

        # HAIR (style and color)
        cabello = config.get("cabello")
        if cabello:
            estilo = tipos_cabello.get(cabello)
            color = colores_cabello.get(cabello)
            if estilo:
                avatar.top_type = estilo
            if color:
                avatar.hair_color = color

        # CLOTHING
        ropa = config.get("ropa")
        if ropa:
            tipo = tipos_ropa.get(ropa)
            color = colores_ropa.get(ropa)
            if tipo:
                avatar.clothe_type = tipo
            if color:
                avatar.clothe_color = color

        # SKIN COLOR
        piel = config.get("piel")
        if piel:
            color_piel = colores_piel.get(piel)
            if color_piel:
                avatar.skin_color = color_piel


        # MOUTH
        boca = config.get("boca")
        if boca:
            tipo = tipos_boca.get(boca)
            if tipo:
                avatar.mouth_type = tipo

        # EYES
        ojos = config.get("ojos")
        if ojos:
            tipo = tipos_ojos.get(ojos)
            if tipo:
                avatar.eye_type = tipo

        # EYEBROWS
        cejas = config.get("cejas")
        if cejas:
            tipo = tipos_cejas.get(cejas)
            if tipo:
                avatar.eyebrow_type = tipo

        # ACCESSORIES
        accesorio = config.get("accesorio")
        if accesorio and accesorio != "ninguno":
            tipo = tipos_accesorios.get(accesorio)
            if tipo:
                avatar.accessories_type = tipo

        avatar.render_png_file(output_path)
        print(f"Avatar successfully generated: {output_path}")

    def show_avatar(self, image_path: str):
        root = tk.Tk()
        root.title("Generated Avatar")

        img = Image.open(image_path)
        img = img.resize((300, 300))
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(root, image=photo)
        label.pack(padx=20, pady=20)

        root.mainloop()