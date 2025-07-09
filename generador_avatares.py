import re
import py_avataaars as pa
print(dir(pa))

# Extended Dictionaries
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
    "rubio_dorado": pa.HairColor.BLONDE_GOLDEN,
    "castaño": pa.HairColor.BROWN,
    "castaño_oscuro": pa.HairColor.BROWN_DARK,
    "rosado_pastel": pa.HairColor.PASTEL_PINK,
    "platinado": pa.HairColor.PLATINUM,
    "rojo": pa.HairColor.RED,
    "gris": pa.HairColor.SILVER_GRAY
}

tipos_cabello = {
    "calvo": pa.TopType.NO_HAIR,
    "parche": pa.TopType.EYE_PATCH,
    "hiyab": pa.TopType.HIJAB,
    "turbante": pa.TopType.TURBAN,
    "gorro1": pa.TopType.WINTER_HAT1,
    "gorro2": pa.TopType.WINTER_HAT2,
    "gorro3": pa.TopType.WINTER_HAT3,
    "gorro4": pa.TopType.WINTER_HAT4,
    "voluminoso": pa.TopType.LONG_HAIR_BIG_HAIR,
    "bob": pa.TopType.LONG_HAIR_BOB,
    "moño": pa.TopType.LONG_HAIR_BUN,
    "largo_rizado": pa.TopType.LONG_HAIR_CURLY,
    "largo_ondulado": pa.TopType.LONG_HAIR_CURVY,
    "dreadlocks_largos": pa.TopType.LONG_HAIR_DREADS,
    "frida": pa.TopType.LONG_HAIR_FRIDA,
    "afro": pa.TopType.LONG_HAIR_FRO,
    "afro_cinta": pa.TopType.LONG_HAIR_FRO_BAND,
    "medio_largo": pa.TopType.LONG_HAIR_NOT_TOO_LONG,
    "mia": pa.TopType.LONG_HAIR_MIA_WALLACE,
    "rapado_lados": pa.TopType.LONG_HAIR_SHAVED_SIDES,
    "liso": pa.TopType.LONG_HAIR_STRAIGHT,
    "liso2": pa.TopType.LONG_HAIR_STRAIGHT2,
    "mechón": pa.TopType.LONG_HAIR_STRAIGHT_STRAND,
    "dreadlocks1": pa.TopType.SHORT_HAIR_DREADS_01,
    "dreadlocks2": pa.TopType.SHORT_HAIR_DREADS_02,
    "esponjado": pa.TopType.SHORT_HAIR_FRIZZLE,
    "mullet": pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
    "corto_rizado": pa.TopType.SHORT_HAIR_SHORT_CURLY,
    "corto_plano": pa.TopType.SHORT_HAIR_SHORT_FLAT,
    "corto_redondo": pa.TopType.SHORT_HAIR_SHORT_ROUND,
    "corto_ondulado": pa.TopType.SHORT_HAIR_SHORT_WAVED,
    "corte_lados": pa.TopType.SHORT_HAIR_SIDES,
    "cesar": pa.TopType.SHORT_HAIR_THE_CAESAR,
    "cesar_lado": pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART
}

colores_ropa = {
    "negro": pa.Color.BLACK,
    "azul": pa.Color.BLUE_01,
    "azul2": pa.Color.BLUE_02,
    "gris": pa.Color.GRAY_01,
    "gris_claro": pa.Color.GRAY_02,
    "blanco": pa.Color.WHITE,
    "rojo": pa.Color.RED,
    "rosado": pa.Color.PINK,
    "pastel_azul": pa.Color.PASTEL_BLUE,
    "pastel_verde": pa.Color.PASTEL_GREEN,
    "pastel_naranja": pa.Color.PASTEL_ORANGE,
    "pastel_rojo": pa.Color.PASTEL_RED,
    "pastel_amarillo": pa.Color.PASTEL_YELLOW,
    "heather": pa.Color.HEATHER
}

tipos_boca = {
    "neutral": pa.MouthType.DEFAULT,
    "feliz": pa.MouthType.SMILE,
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
    "ojos_en_blanco": pa.EyesType.EYE_ROLL,
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
    "enojadas_naturales": pa.EyebrowType.ANGRY_NATURAL,
    "planas": pa.EyebrowType.FLAT_NATURAL,
    "levantadas": pa.EyebrowType.RAISED_EXCITED,
    "levantadas_naturales": pa.EyebrowType.RAISED_EXCITED_NATURAL,
    "tristes": pa.EyebrowType.SAD_CONCERNED,
    "tristes_naturales": pa.EyebrowType.SAD_CONCERNED_NATURAL,
    "uniceja": pa.EyebrowType.UNI_BROW_NATURAL,
    "arriba_y_abajo": pa.EyebrowType.UP_DOWN,
    "arriba_y_abajo_natural": pa.EyebrowType.UP_DOWN_NATURAL,
    "fruncidas": pa.EyebrowType.FROWN_NATURAL
}

tipos_accesorios = {
    "ninguno": pa.AccessoriesType.DEFAULT,
    "gafas_redondas": pa.AccessoriesType.ROUND,
    "gafas_sol": pa.AccessoriesType.SUNGLASSES,
}

tipos_ropa = {
    "blazer_camisa": pa.ClotheType.BLAZER_SHIRT,
    "blazer_suéter": pa.ClotheType.BLAZER_SWEATER,
    "cuello_suéter": pa.ClotheType.COLLAR_SWEATER,
    "camiseta_gráfica": pa.ClotheType.GRAPHIC_SHIRT,
    "hoodie": pa.ClotheType.HOODIE,
    "overol": pa.ClotheType.OVERALL,
    "camiseta_cuello_redondo": pa.ClotheType.SHIRT_CREW_NECK,
    "cuello_scoop": pa.ClotheType.SHIRT_SCOOP_NECK,
    "cuello_v": pa.ClotheType.SHIRT_V_NECK
}