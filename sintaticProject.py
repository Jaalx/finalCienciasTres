# LANGUAGE GRAMMAR

# <PROGRAMA>         -> "inicio" <INSTRUCCIONES> "final"
# <INSTRUCCIONES>    -> <INSTRUCCION> ";" <INSTRUCCIONES> | <INSTRUCCION> ";"
# <INSTRUCCION>      -> <VERBO> <ATRIBUTO> <VALOR>
# <VERBO>            -> "teñir" | "ajustar" | "añadir" | "expresar"
# <ATRIBUTO>         -> "cabello" | "ropa" | "boca" | "ojos" | "cejas" | "accesorio"
# <VALOR>            -> <COLOR_CABELLO> | <COLOR_ROPA> | <ESTILO_CABELLO> | <TIPO_ROPA> | <EXPRESION> | <ACCESORIO>
# <COLOR_CABELLO>    -> "negro" | "cobrizo" | "rubio" | "rubio_dorado" | "castaño" | "castaño_oscuro"
#                      | "rosado_pastel" | "platinado" | "rojo" | "gris"
# <COLOR_ROPA>       -> "negro" | "azul" | "azul2" | "gris" | "gris_claro" | "blanco" | "rojo" | "rosado"
#                      | "pastel_azul" | "pastel_verde" | "pastel_naranja" | "pastel_rojo"
#                      | "pastel_amarillo" | "heather"
# <ESTILO_CABELLO>   -> "calvo" | "parche" | "sombrero" | "hiyab" | "turbante" | "gorro1" | "gorro2" | "gorro3" | "gorro4"
#                      | "voluminoso" | "bob" | "moño" | "largo_rizado" | "largo_ondulado" | "dreadlocks_largos"
#                      | "frida" | "afro" | "afro_cinta" | "medio_largo" | "mia" | "rapado_lados"
#                      | "liso" | "liso2" | "mechón" | "dreadlocks1" | "dreadlocks2" | "esponjado"
#                      | "mullet" | "corto_rizado" | "corto_plano" | "corto_redondo" | "corto_ondulado"
#                      | "corte_lados" | "cesar" | "cesar_lado"
# <TIPO_ROPA>        -> "blazer_camisa" | "blazer_suéter" | "cuello_suéter" | "camiseta_gráfica"
#                      | "hoodie" | "overol" | "camiseta_cuello_redondo" | "cuello_scoop" | "cuello_v"
# <EXPRESION>        -> "neutral" | "preocupado" | "incrédulo" | "comiendo" | "frunciéndo" | "triste"
#                      | "gritando" | "serio" | "sonriente" | "lengua" | "brillo" | "vómito" | "feliz"
# <ACCESORIO>        -> "ninguno" | "gafas_redondas" | "gafas_sol"

class ParserError(Exception):
    pass

class SyntacticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.current_token = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        self.program()

    def match(self, expected_type):
        if self.current_token and self.current_token.type_ == expected_type:
            self.advance()
        else:
            raise ParserError(f"Se esperaba {expected_type}, pero se encontró {self.current_token}")

    def program(self):
        self.match("KEYWORD")  # 'inicio'
        self.instructions()
        self.match("KEYWORD")  # 'final'
        if self.current_token is not None:
            raise ParserError(f"Tokens inesperados después de 'final': {self.current_token}")

    def instructions(self):
        self.instruction()
        while self.current_token and self.current_token.type_ == "SEPARADOR":
            self.match("SEPARADOR")
            if self.current_token and self.current_token.type_ == "VERBO":
                self.instruction()

    def instruction(self):
        self.match("VERBO")
        self.match("ATRIBUTO")
        self.value()

    def value(self):
        valid_types = {
            "COLOR_PIEL", "COLOR_CABELLO", "COLOR_ROPA", "COLOR_SOMBRERO",
            "ESTILO_CABELLO", "TIPO_ROPA", "EXPRESION", "ACCESORIO"
        }
        if self.current_token and self.current_token.type_ in valid_types:
            self.advance()
        else:
            raise ParserError(f"Valor inesperado: {self.current_token}")


# Syntactic analyzer test
if __name__ == "__main__":
    from lexicalProject import LexicalAnalyzer

    def test_parser():
        entrada = """
        inicio
        teñir cabello castaño_oscuro;
        ajustar ropa hoodie;
        añadir accesorio gafas_redondas;
        expresar boca sonriente;
        final
        """
        tokens = LexicalAnalyzer.lex(entrada)
        parser = SyntacticAnalyzer(tokens)
        parser.parse()
        print("Análisis sintáctico exitoso.")

    test_parser()