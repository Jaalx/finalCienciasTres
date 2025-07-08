class SemanticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.avatar_config = {
            "cabello": None,
            "ropa": None,
            "boca": None,
            "ojos": None,
            "cejas": None,
            "accesorio": None,
            "piel": None
        }

        self.verbo_atributos_permitidos = {
            "teñir": {"cabello","ropa"},
            "ajustar": {"ropa", "piel", "cabello"},
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
                    raise ValueError("Incomplete instruction near: " + str(token))

                verbo = self.tokens[i].value
                atributo = self.tokens[i + 1].value
                valor = self.tokens[i + 2].value

                if atributo not in self.avatar_config:
                    raise ValueError(f"Unknown attribute: {atributo}")

                if atributo not in self.verbo_atributos_permitidos.get(verbo, set()):
                    raise ValueError(f"The verb '{verbo}' cannot be used with the attribute '{atributo}'")

                self.avatar_config[atributo] = valor
                i += 3
                continue

            raise ValueError(f"Unexpected value: {token}")

        return self.avatar_config