from generador_avatares import (
    colores_cabello, tipos_cabello, colores_ropa, tipos_ropa,
    tipos_boca, tipos_ojos, tipos_cejas, tipos_accesorios, colores_piel
)

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
            "teñir": {"cabello", "ropa"},
            "ajustar": {"ropa", "piel", "cabello"},
            "añadir": {"accesorio"},
            "expresar": {"boca", "ojos", "cejas"}
        }

        self.valores_validos = {
            "piel": set(colores_piel.keys()),
            "cabello": set(colores_cabello.keys()).union(tipos_cabello.keys()),
            "ropa": set(colores_ropa.keys()).union(tipos_ropa.keys()),
            "boca": set(tipos_boca.keys()),
            "ojos": set(tipos_ojos.keys()),
            "cejas": set(tipos_cejas.keys()),
            "accesorio": set(tipos_accesorios.keys())
        }

    def analyze(self):
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]

            if token.type_ in {"SEPARADOR", "KEYWORD"}:
                i += 1
                continue

            if token.type_ == "VERBO":
                if i + 2 >= len(self.tokens):
                    raise ValueError("Incomplete instruction near: " + str(token))

                verbo = token.value
                atributo = self.tokens[i + 1].value
                valor = self.tokens[i + 2].value

                if atributo not in {"cabello", "ropa", "boca", "ojos", "cejas", "accesorio", "piel"}:
                    raise ValueError(f"Unknown attribute: {atributo}")

                if atributo not in self.verbo_atributos_permitidos.get(verbo, set()):
                    raise ValueError(f"The verb '{verbo}' cannot be used with the attribute '{atributo}'")

                if atributo == "cabello":
                    if valor in colores_cabello:
                        self.avatar_config["cabello_color"] = valor
                    elif valor in tipos_cabello:
                        self.avatar_config["cabello_tipo"] = valor
                    else:
                        raise ValueError(f"Invalid value '{valor}' for attribute '{atributo}'")

                elif atributo == "ropa":
                    if valor in colores_ropa:
                        self.avatar_config["ropa_color"] = valor
                    elif valor in tipos_ropa:
                        self.avatar_config["ropa_tipo"] = valor
                    else:
                        raise ValueError(f"Invalid value '{valor}' for attribute '{atributo}'")

                elif atributo == "piel":
                    if valor in colores_piel:
                        self.avatar_config["piel"] = valor
                    else:
                        raise ValueError(f"Invalid value '{valor}' for attribute '{atributo}'")

                elif atributo == "boca":
                    if valor in tipos_boca:
                        self.avatar_config["boca"] = valor
                    else:
                        raise ValueError(f"Invalid value '{valor}' for attribute '{atributo}'")

                elif atributo == "ojos":
                    if valor in tipos_ojos:
                        self.avatar_config["ojos"] = valor
                    else:
                        raise ValueError(f"Invalid value '{valor}' for attribute '{atributo}'")

                elif atributo == "cejas":
                    if valor in tipos_cejas:
                        self.avatar_config["cejas"] = valor
                    else:
                        raise ValueError(f"Invalid value '{valor}' for attribute '{atributo}'")

                elif atributo == "accesorio":
                    if valor in tipos_accesorios:
                        self.avatar_config["accesorio"] = valor
                    else:
                        raise ValueError(f"Invalid value '{valor}' for attribute '{atributo}'")

                i += 3
                continue

            raise ValueError(f"Unexpected value: {token}")

        return self.avatar_config
