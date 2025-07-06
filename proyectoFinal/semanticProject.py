class SemanticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.avatar_config = {
            "cabello": None,
            "ropa": None,
            "boca": None,
            "ojos": None,
            "cejas": None,
            "accesorio": None
        }

        self.verbo_atributos_permitidos = {
            "teñir": {"cabello"},
            "ajustar": {"ropa"},
            "añadir": {"accesorio"},
            "expresar": {"boca", "ojos", "cejas"}
        }

    def analyze(self):
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]

            if token.type_ == "SEPARADOR":
                i += 1
                continue

            if token.type_ == "KEYWORD":
                i += 1
                continue

            if token.type_ == "VERBO":
                if i + 2 >= len(self.tokens):
                    raise ValueError("Instrucción incompleta cerca de: " + str(token))

                verbo = self.tokens[i].value
                atributo = self.tokens[i + 1].value
                valor = self.tokens[i + 2].value

                if atributo not in self.avatar_config:
                    raise ValueError(f"Atributo desconocido: {atributo}")

                if atributo not in self.verbo_atributos_permitidos.get(verbo, set()):
                    raise ValueError(f"El verbo '{verbo}' no puede usarse con el atributo '{atributo}'")

                self.avatar_config[atributo] = valor
                i += 3
                continue

            raise ValueError(f"Valor inesperado: {token}")

        return self.avatar_config


# ---------------------
# PRUEBA DEL SEMÁNTICO
# ---------------------
if __name__ == "__main__":
    from lexicalProject import LexicalAnalyzer
    from sintaticProject import SyntacticAnalyzer

    def test_semantic_analysis():
        print("\nPRUEBA CON ENTRADA VÁLIDA:")
        good_input = """
        inicio
        teñir cabello castaño_oscuro;
        ajustar ropa hoodie;
        añadir accesorio gafas_redondas;
        expresar boca sonriente;
        expresar ojos feliz;
        final
        """
        try:
            tokens = LexicalAnalyzer.lex(good_input)
            SyntacticAnalyzer(tokens).parse()
            config = SemanticAnalyzer(tokens).analyze()
            print("Análisis semántico exitoso.")
            print("Configuración:", config)
        except Exception as e:
            print("Error:", e)

        print("\nPRUEBA CON ENTRADA INVÁLIDA:")
        bad_input = """
        inicio
        teñir ropa azul;
        final
        """
        try:
            tokens = LexicalAnalyzer.lex(bad_input)
            SyntacticAnalyzer(tokens).parse()
            config = SemanticAnalyzer(tokens).analyze()
            print("Análisis semántico exitoso.")
            print("Configuración:", config)
        except Exception as e:
            print("Error:", e)

    test_semantic_analysis()
