import re

class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type_}, {self.value})"

class LexicalAnalyzer:
    @staticmethod
    def lex(code: str):
        tokens = []

        token_specification = [
            ("KEYWORD", r'\b(inicio|final)\b'),
            ("VERBO", r'\b(teñir|ajustar|añadir|expresar)\b'),
            ("ATRIBUTO", r'\b(cabello|ropa|boca|ojos|cejas|accesorio)\b'),

            ("COLOR_PIEL", r'\b(negra|bronceada|amarilla|pálida|clara|trigueña|oscura)\b'),
            ("COLOR_CABELLO", r'\b(negro|cobrizo|rubio|rubio_dorado|castaño|castaño_oscuro|rosado_pastel|platinado|rojo|gris)\b'),
            ("COLOR_ROPA", r'\b(negro|azul|azul2|gris|gris_claro|blanco|rojo|rosado|pastel_azul|pastel_verde|pastel_naranja|pastel_rojo|pastel_amarillo|heather)\b'),
            ("COLOR_SOMBRERO", r'\b(negro|azul|azul2|gris|gris_claro|blanco|rojo|rosado|pastel_azul|pastel_verde|pastel_naranja|pastel_rojo|pastel_amarillo|heather)\b'),

            ("ESTILO_CABELLO", r'\b(calvo|parche|sombrero|hiyab|turbante|gorro1|gorro2|gorro3|gorro4|voluminoso|bob|moño|largo_rizado|largo_ondulado|dreadlocks_largos|frida|afro|afro_cinta|medio_largo|mia|rapado_lados|liso|liso2|mechón|dreadlocks1|dreadlocks2|esponjado|mullet|corto_rizado|corto_plano|corto_redondo|corto_ondulado|corte_lados|cesar|cesar_lado)\b'),
            ("TIPO_ROPA", r'\b(blazer_camisa|blazer_suéter|cuello_suéter|camiseta_gráfica|hoodie|overol|camiseta_cuello_redondo|cuello_scoop|cuello_v)\b'),

            ("EXPRESION", r'\b(neutral|preocupado|incrédulo|comiendo|frunciéndo|triste|gritando|serio|sonriente|lengua|brillo|vómito|feliz)\b'),
            ("ACCESORIO", r'\b(gafas_redondas|gafas_sol|ninguno)\b'),

            ("SEPARADOR", r';'),
            ("SKIP", r'[ \t\n]+'),
            ("MISSMATCH", r'.'),
        ]

        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == "SKIP":
                continue
            elif kind == "MISSMATCH":
                raise RuntimeError(f"Caracter inesperado: {value}")
            else:
                tokens.append(Token(kind, value))
        return tokens
