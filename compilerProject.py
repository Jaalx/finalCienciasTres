from lexicalProject import LexicalAnalyzer
from sintaticProject import SyntacticAnalyzer
from semanticProject import SemanticAnalyzer
import python_avatars as pa

# Importamos todos los diccionarios de mapeo
from generador_avatares import (
    colores_cabello, tipos_cabello, colores_ropa, tipos_ropa, tipos_boca,
    tipos_ojos, tipos_cejas, accesorios as tipos_accesorios, colores_piel
)


class Compiler:
    def compile(self, code: str):
        # Etapas del compilador
        tokens = LexicalAnalyzer.lex(code)
        SyntacticAnalyzer(tokens).parse()
        avatar_config = SemanticAnalyzer(tokens).analyze()
        print("Configuración de avatar:", avatar_config)

        # Generar avatar usando py_avataaars
        self.generate_avatar(avatar_config)

    def generate_avatar(self, config: dict):
        # Valores por defecto
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

        # CABELO (estilo y color)
        cabello = config.get("cabello")
        if cabello:
            estilo = tipos_cabello.get(cabello)
            color = colores_cabello.get(cabello)
            if estilo:
                avatar.top_type = estilo
            if color:
                avatar.hair_color = color

        # ROPA
        ropa = config.get("ropa")
        if ropa:
            tipo = tipos_ropa.get(ropa)
            color = colores_ropa.get(ropa)
            if tipo:
                avatar.clothe_type = tipo
            if color:
                avatar.clothe_color = color

        # BOCA
        boca = config.get("boca")
        if boca:
            tipo = tipos_boca.get(boca)
            if tipo:
                avatar.mouth_type = tipo

        # OJOS
        ojos = config.get("ojos")
        if ojos:
            tipo = tipos_ojos.get(ojos)
            if tipo:
                avatar.eye_type = tipo

        # CEJAS
        cejas = config.get("cejas")
        if cejas:
            tipo = tipos_cejas.get(cejas)
            if tipo:
                avatar.eyebrow_type = tipo

        # ACCESORIOS
        accesorio = config.get("accesorio")
        if accesorio and accesorio != "ninguno":
            tipo = tipos_accesorios.get(accesorio)
            if tipo:
                avatar.accessories_type = tipo

        # Guardar imagen
        output_path = "avatar_result.png"
        avatar.render_png_file(output_path)
        print(f"✅ Avatar generado con éxito: {output_path}")
