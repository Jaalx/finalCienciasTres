import re
import python_avatars as pa
print(dir(pa))

# Diccionarios ampliados
avatar_styles = {
    "transparente": pa.AvatarStyle.TRANSPARENT,
    "círculo": pa.AvatarStyle.CIRCLE
}

colores_piel = {
    "negra": pa.SkinColor.BLACK,
    "bronceada": pa.SkinColor.TANNED,
    "amarilla": pa.SkinColor.YELLOW,
    "pálida": pa.SkinColor.PALE,
    "clara": pa.SkinColor.LIGHT,
    "trigueña": pa.SkinColor.BROWN,
    "oscura": pa.SkinColor.DARK_BROWN
}

colores_cabello = {
    "negro": pa.HairColor.BLACK,
    "cobrizo": pa.HairColor.AUBURN,
    "rubio": pa.HairColor.BLONDE,
    "rubio dorado": pa.HairColor.BLONDE_GOLDEN,
    "castaño": pa.HairColor.BROWN,
    "castaño oscuro": pa.HairColor.BROWN_DARK,
    "rosado pastel": pa.HairColor.PASTEL_PINK,
    "platinado": pa.HairColor.PLATINUM,
    "rojo": pa.HairColor.RED,
    "gris": pa.HairColor.SILVER_GRAY
}

tipos_cabello = {
    "calvo": pa.TopType.NO_HAIR,
    "parche": pa.TopType.EYE_PATCH,
    "sombrero": pa.TopType.HAT,
    "hiyab": pa.TopType.HIJAB,
    "turbante": pa.TopType.TURBAN,
    "gorro1": pa.TopType.WINTER_HAT1,
    "gorro2": pa.TopType.WINTER_HAT2,
    "gorro3": pa.TopType.WINTER_HAT3,
    "gorro4": pa.TopType.WINTER_HAT4,
    "voluminoso": pa.TopType.LONG_HAIR_BIG_HAIR,
    "bob": pa.TopType.LONG_HAIR_BOB,
    "moño": pa.TopType.LONG_HAIR_BUN,
    "largo rizado": pa.TopType.LONG_HAIR_CURLY,
    "largo ondulado": pa.TopType.LONG_HAIR_CURVY,
    "dreadlocks largos": pa.TopType.LONG_HAIR_DREADS,
    "frida": pa.TopType.LONG_HAIR_FRIDA,
    "afro": pa.TopType.LONG_HAIR_FRO,
    "afro cinta": pa.TopType.LONG_HAIR_FRO_BAND,
    "medio largo": pa.TopType.LONG_HAIR_NOT_TOO_LONG,
    "mia": pa.TopType.LONG_HAIR_MIA_WALLACE,
    "rapado lados": pa.TopType.LONG_HAIR_SHAVED_SIDES,
    "liso": pa.TopType.LONG_HAIR_STRAIGHT,
    "liso2": pa.TopType.LONG_HAIR_STRAIGHT2,
    "mechón": pa.TopType.LONG_HAIR_STRAIGHT_STRAND,
    "dreadlocks1": pa.TopType.SHORT_HAIR_DREADS_01,
    "dreadlocks2": pa.TopType.SHORT_HAIR_DREADS_02,
    "esponjado": pa.TopType.SHORT_HAIR_FRIZZLE,
    "mullet": pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
    "corto rizado": pa.TopType.SHORT_HAIR_SHORT_CURLY,
    "corto plano": pa.TopType.SHORT_HAIR_SHORT_FLAT,
    "corto redondo": pa.TopType.SHORT_HAIR_SHORT_ROUND,
    "corto ondulado": pa.TopType.SHORT_HAIR_SHORT_WAVED,
    "corte lados": pa.TopType.SHORT_HAIR_SIDES,
    "cesar": pa.TopType.SHORT_HAIR_THE_CAESAR,
    "cesar lado": pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART
}

colores_sombrero = {
    "negro": pa.Color.BLACK,
    "azul": pa.Color.BLUE_01,
    "azul2": pa.Color.BLUE_02,
    "gris": pa.Color.GRAY_01,
    "gris claro": pa.Color.GRAY_02,
    "blanco": pa.Color.WHITE,
    "rojo": pa.Color.RED,
    "rosado": pa.Color.PINK,
    "pastel azul": pa.Color.PASTEL_BLUE,
    "pastel verde": pa.Color.PASTEL_GREEN,
    "pastel naranja": pa.Color.PASTEL_ORANGE,
    "pastel rojo": pa.Color.PASTEL_RED,
    "pastel amarillo": pa.Color.PASTEL_YELLOW,
    "heather": pa.Color.HEATHER
}

# Colores de ropa
colores_ropa = {
    "negro": pa.Color.BLACK,
    "azul": pa.Color.BLUE_01,
    "azul2": pa.Color.BLUE_02,
    "gris": pa.Color.GRAY_01,
    "gris claro": pa.Color.GRAY_02,
    "blanco": pa.Color.WHITE,
    "rojo": pa.Color.RED,
    "rosado": pa.Color.PINK,
    "pastel azul": pa.Color.PASTEL_BLUE,
    "pastel verde": pa.Color.PASTEL_GREEN,
    "pastel naranja": pa.Color.PASTEL_ORANGE,
    "pastel rojo": pa.Color.PASTEL_RED,
    "pastel amarillo": pa.Color.PASTEL_YELLOW,
    "heather": pa.Color.HEATHER
}

tipos_barba = {
    "sin barba": pa.FacialHairType.DEFAULT,
    "barba media": pa.FacialHairType.BEARD_MEDIUM,
    "barba corta": pa.FacialHairType.BEARD_LIGHT,
    "barba larga": pa.FacialHairType.BEARD_MAJESTIC,
    "bigote fino": pa.FacialHairType.MOUSTACHE_FANCY,
    "bigote grueso": pa.FacialHairType.MOUSTACHE_MAGNUM
}

tipos_boca = {
    "neutral": pa.MouthType.DEFAULT,
    "preocupado": pa.MouthType.CONCERNED,
    "incrédulo": pa.MouthType.DISBELIEF,
    "comiendo": pa.MouthType.EATING,
    "frunciéndo": pa.MouthType.GRIMACE,
    "triste": pa.MouthType.SAD,
    "gritando": pa.MouthType.SCREAM_OPEN,
    "serio": pa.MouthType.SERIOUS,
    "sonriente": pa.MouthType.SMILE,
    "lengua": pa.MouthType.TONGUE,
    "brillo": pa.MouthType.TWINKLE,
    "vómito": pa.MouthType.VOMIT
}

tipos_ojos = {
    "neutros": pa.EyesType.DEFAULT,
    "cerrados": pa.EyesType.CLOSE,
    "llorando": pa.EyesType.CRY,
    "mareados": pa.EyesType.DIZZY,
    "ojos en blanco": pa.EyesType.EYE_ROLL,
    "felices": pa.EyesType.HAPPY,
    "enamorados": pa.EyesType.HEARTS,
    "laterales": pa.EyesType.SIDE,
    "entrecerrados": pa.EyesType.SQUINT,
    "sorprendidos": pa.EyesType.SURPRISED,
    "guiño": pa.EyesType.WINK,
    "loco": pa.EyesType.WINK_WACKY
}

tipos_cejas = {
    "neutras": pa.EyebrowType.DEFAULT,
    "naturales": pa.EyebrowType.DEFAULT_NATURAL,
    "enojadas": pa.EyebrowType.ANGRY,
    "enojadas naturales": pa.EyebrowType.ANGRY_NATURAL,
    "planas": pa.EyebrowType.FLAT_NATURAL,
    "levantadas": pa.EyebrowType.RAISED_EXCITED,
    "levantadas naturales": pa.EyebrowType.RAISED_EXCITED_NATURAL,
    "tristes": pa.EyebrowType.SAD_CONCERNED,
    "tristes naturales": pa.EyebrowType.SAD_CONCERNED_NATURAL,
    "uniceja": pa.EyebrowType.UNI_BROW_NATURAL,
    "arriba y abajo": pa.EyebrowType.UP_DOWN,
    "arriba y abajo natural": pa.EyebrowType.UP_DOWN_NATURAL,
    "fruncidas": pa.EyebrowType.FROWN_NATURAL
}

tipos_nariz = {
    "normal": pa.NoseType.DEFAULT
}

accesorios = {
    "ninguno": pa.AccessoriesType.DEFAULT,
    "kurt": pa.AccessoriesType.KURT,
    "gafas receta 1": pa.AccessoriesType.PRESCRIPTION_01,
    "gafas receta 2": pa.AccessoriesType.PRESCRIPTION_02,
    "redondas": pa.AccessoriesType.ROUND,
    "sol": pa.AccessoriesType.SUNGLASSES,
    "wayfarers": pa.AccessoriesType.WAYFARERS
}

tipos_ropa = {
    "blazer camisa": pa.ClotheType.BLAZER_SHIRT,
    "blazer suéter": pa.ClotheType.BLAZER_SWEATER,
    "cuello suéter": pa.ClotheType.COLLAR_SWEATER,
    "camiseta gráfica": pa.ClotheType.GRAPHIC_SHIRT,
    "hoodie": pa.ClotheType.HOODIE,
    "overol": pa.ClotheType.OVERALL,
    "camiseta cuello redondo": pa.ClotheType.SHIRT_CREW_NECK,
    "cuello scoop": pa.ClotheType.SHIRT_SCOOP_NECK,
    "cuello v": pa.ClotheType.SHIRT_V_NECK
}

graficos_camiseta = {
    "murciélago": pa.ClotheGraphicType.BAT,
    "cumbia": pa.ClotheGraphicType.CUMBIA,
    "ciervo": pa.ClotheGraphicType.DEER,
    "diamante": pa.ClotheGraphicType.DIAMOND,
    "hola": pa.ClotheGraphicType.HOLA,
    "pizza": pa.ClotheGraphicType.PIZZA,
    "resistir": pa.ClotheGraphicType.RESIST,
    "selena": pa.ClotheGraphicType.SELENA,
    "oso": pa.ClotheGraphicType.BEAR,
    "calavera contorno": pa.ClotheGraphicType.SKULL_OUTLINE,
    "calavera": pa.ClotheGraphicType.SKULL
}

def mostrar_opciones():
    print("""
🎨 OPCIONES DISPONIBLES PARA DESCRIPCIÓN ENTRE PARÉNTESIS

┌──────────────────────────────┬───────────────────────────────────────────────┐
│        Categoría             │                   Opciones                    │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Estilos de avatar            │ transparente, círculo                         │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Colores de piel              │ negra, trigueña, clara, amarilla, oscura      │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Colores de cabello           │ negro, castaño, rubio, rojo, gris             │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Tipos de cabello/sombrero    │ calvo, liso, rizado, ondulado, dreadlocks     │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Tipo de barba                │ sin barba, barba corta, barba larga, bigote   │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Colores de ropa              │ blanca, negra, roja, azul, gris               │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Tipos de ropa                │ camiseta, hoodie, blazer, camisa              │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Accesorios                   │ gafas redondas, gafas sol, sin accesorios     │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Tipos de nariz               │ predeterminada                                │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Tipos de cejas               │ normales, fruncidas, sorprendidas, uniceja    │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Tipos de ojos                │ normales, corazón, cerrados, llorosos         │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Tipos de boca                │ normal, sonriente, triste, abierta            │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Color de sombrero            │ negro, rojo, azul, blanco, pastel             │
├──────────────────────────────┼───────────────────────────────────────────────┤
│ Gráfico en la camiseta       │ murciélago, calavera, pizza, hola             │
└──────────────────────────────┴───────────────────────────────────────────────┘

📌 Ejemplo válido:
(Cabello color rojo rizado) (Piel negra) (Barba larga) (Ropa blanca) (Ojos corazón) (Estilo círculo)
""")
    
# Expresiones regulares por bloque
patrones = {
    "cabello": re.compile(r'\(cabello color (?P<color>\w+)(?: (?P<tipo>[\w\s]+))?\)', re.IGNORECASE),
    "piel": re.compile(r'\(piel (?P<color>\w+)\)', re.IGNORECASE),
    "barba": re.compile(r'\((?P<tipo>barba larga|barba media|barba corta|bigote|sin barba)\)', re.IGNORECASE),
    "ropa": re.compile(r'\(ropa (?P<color>\w+)\)', re.IGNORECASE),
    "tipo_ropa": re.compile(r'\(tipo de ropa (?P<tipo>[\w\s]+?)\)', re.IGNORECASE),
    "accesorios": re.compile(r'\(accesorio (?P<tipo>[\w\s]+?)\)', re.IGNORECASE),
    "nariz": re.compile(r'\(nariz (?P<tipo>\w+)\)', re.IGNORECASE),
    "cejas": re.compile(r'\(cejas (?P<tipo>[\w\s]+?)\)', re.IGNORECASE),
    "ojos": re.compile(r'\(ojos (?P<tipo>[\w\s]+?)\)', re.IGNORECASE),
    "boca": re.compile(r'\(boca (?P<tipo>[\w\s]+?)\)', re.IGNORECASE),
    "sombrero_color": re.compile(r'\(sombrero color (?P<color>\w+)\)', re.IGNORECASE),
    "grafico": re.compile(r'\(grafico (?P<tipo>[\w\s]+?)\)', re.IGNORECASE),
    "estilo": re.compile(r'\(estilo (?P<tipo>\w+)\)', re.IGNORECASE)
}

def main():
    mostrar_opciones()
    entrada = input("\n✏️ Escribe la descripción del avatar entre paréntesis: ").strip().lower()
    bloques = re.findall(r"\(.*?\)", entrada)

    # Valores por defecto
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
            accessories = accesorios.get(tipo, accessories)
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
        elif match := patrones["sombrero_color"].fullmatch(bloque):
            color = match.group("color")
            hat_color = colores_sombrero.get(color, hat_color)
        elif match := patrones["grafico"].fullmatch(bloque):
            tipo = match.group("tipo")
            graphic_type = graficos_camiseta.get(tipo, graphic_type)
        elif match := patrones["estilo"].fullmatch(bloque):
            tipo = match.group("tipo")
            avatar_style = avatar_styles.get(tipo, avatar_style)
        else:
            errores.append(f"Bloque no reconocido: {bloque}")

    if errores:
        print("\n❌ Se encontraron los siguientes errores:")
        for err in errores:
            print("-", err)
    else:
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
        avatar.render_png_file("avatar_completo.png")
        print("\n✅ Avatar generado correctamente como 'avatar_completo.png'")

if __name__ == "__main__":
    main()
