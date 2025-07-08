"""This module is just an example of how to use the compiler."""
from compilerProject import Compiler

# ----------------------------------------------
# CUSTOMIZATION OPTIONS FOR AVATARS
# ----------------------------------------------

# VERB -> expresar
# Valid attributes:
#   boca  -> neutral, preocupado, incrédulo, comiendo, frunciéndo, triste,
#            gritando, serio, sonriente, lengua, brillo, vómito
#   ojos  -> neutros, cerrados, llorando, mareados, ojos en blanco, felices,
#            enamorados, laterales, entrecerrados, sorprendidos, guiño, loco
#   cejas -> neutras, naturales, enojadas, enojadas naturales, planas,
#            levantadas, levantadas naturales, tristes, tristes naturales,
#            uniceja, arriba y abajo, arriba y abajo natural, fruncidas

# VERB -> ajustar
# Valid attribute:
#   ropa -> blazer_camisa, blazer_suéter, cuello_suéter, camiseta_gráfica,
#           hoodie, overol, camiseta_cuello_redondo, cuello_scoop, cuello_v

# VERB -> teñir
# Valid attribute:
#   cabello -> negro, cobrizo, rubio, rubio_dorado, castaño,
#              castaño_oscuro, rosado_pastel, platinado, rojo, gris

# VERB -> añadir
# Valid attribute:
#   accesorio -> gafas_redondas, gafas_sol, ninguno


# =========== Example usage ========== #
def example1(compiler_: Compiler):
    """Avatar con cabello platinado, hoodie, gafas y sonrisa."""
    input_text = """
    inicio
    teñir cabello platinado;
    ajustar ropa cuello_v;
    añadir accesorio gafas_sol;
    expresar boca vómito;
    final
    """
    compiler_.compile(input_text)

def example2(compiler_: Compiler):
    """Avatar con cabello castaño, camiseta gráfica, sin accesorios y expresión seria."""
    input_text = """
    inicio
    teñir cabello castaño;
    ajustar ropa camiseta_gráfica;
    añadir accesorio ninguno;
    expresar ojos serio;
    final
    """
    compiler_.compile(input_text)

def example3(compiler_: Compiler):
    """Avatar con cabello rojo, overol y expresión feliz en ojos y boca."""
    input_text = """
    inicio
    teñir cabello rojo;
    ajustar ropa overol;
    expresar ojos feliz;
    expresar boca feliz;
    final
    """
    compiler_.compile(input_text)

def example4(compiler_: Compiler):
    """Avatar calvo, con blazer y gafas redondas, cejas frunciéndo."""
    input_text = """
    inicio
    teñir cabello calvo;
    ajustar ropa blazer_suéter;
    añadir accesorio gafas_redondas;
    expresar cejas frunciéndo;
    final
    """
    compiler_.compile(input_text)

def example5(compiler_: Compiler):
    """Avatar con cabello negro, camiseta cuello V y expresión incrédula."""
    input_text = """
    inicio
    teñir cabello negro;
    ajustar ropa cuello_v;
    expresar ojos incrédulo;
    expresar boca incrédulo;
    final
    """
    compiler_.compile(input_text)


if __name__ == "__main__":
    compiler = Compiler()
    example1(compiler)
    #example2(compiler)
    #example3(compiler)
    #example4(compiler)
    #example5(compiler)
