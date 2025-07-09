"""This module is just an example of how to use the compiler."""
from compilerProject import Compiler

# ----------------------------------------------
# CUSTOMIZATION OPTIONS FOR AVATARS
# ----------------------------------------------

# VERB -> expresar
# Valid attributes:
#   boca  -> brillo, comiendo, feliz, frunciéndo, gritando, incrédulo,
#            lengua, neutral, preocupado, serio, sonriente, triste, vómito
#   ojos  -> cerrados, enamorados, entrecerrados, felices, guiño, loco,
#            laterales, llorando, mareados, neutros, ojos_en_blanco, sorprendidos
#   cejas -> arriba_y_abajo, arriba_y_abajo_natural, enojadas, enojadas_naturales,
#            fruncidas, levantadas, levantadas_naturales, naturales, neutras,
#            planas, tristes, tristes_naturales, uniceja

# VERB -> ajustar
# Valid attributes:
#   cabello -> afro, afro_cinta, bob, calvo, cesar, cesar_lado, corto_ondulado,
#              corto_plano, corto_redondo, corto_rizado, corte_lados, dreadlocks1,
#              dreadlocks2, dreadlocks_largos, esponjado, frida, gorro1, gorro2,
#              gorro3, gorro4, hiyab, largo_ondulado, largo_rizado, liso, liso2,
#              mechón, medio_largo, moño, mullet, mia, parche, rapado_lados,
#              turbante, voluminoso
#   piel -> amarilla, bronceada, clara, negra, oscura, pálida, trigueña
#   ropa -> blazer_camisa, blazer_suéter, camiseta_cuello_redondo,
#           camiseta_gráfica, cuello_scoop, cuello_suéter, cuello_v,
#           hoodie, overol

# VERB -> teñir
# Valid attributes:
#   cabello -> castaño, castaño_oscuro, cobrizo, gris, negro,
#              platinado, rojo, rosado_pastel, rubio, rubio_dorado
#   ropa    -> azul, azul2, blanco, gris, gris_claro, heather, negro,
#              pastel_amarillo, pastel_azul, pastel_naranja, pastel_rojo,
#              pastel_verde, rojo, rosado

# VERB -> añadir
# Valid attributes:
#   accesorio -> gafas_redondas, gafas_sol, ninguno



# =========== Example usage ========== #
def example1(compiler_: Compiler):
    """Avatar con cabello afro rojo, piel trigueña, hoodie pastel azul, gafas de sol, cejas fruncidas y ojos sorprendidos."""
    input_text = """
    inicio
    ajustar piel trigueña;
    teñir cabello rojo;
    ajustar cabello afro;
    teñir ropa pastel_azul;
    ajustar ropa hoodie;
    añadir accesorio gafas_sol;
    expresar cejas fruncidas;
    expresar ojos sorprendidos;
    expresar boca gritando;
    final
    """
    compiler_.compile(input_text)

def example2(compiler_: Compiler):
    """Avatar con cabello corto plano platinado, piel clara, blazer suéter gris, cejas planas y ojos cerrados."""
    input_text = """
    inicio
    ajustar piel clara;
    teñir cabello platinado;
    ajustar cabello afro;
    teñir ropa rosado;
    ajustar ropa cuello_v;
    expresar cejas planas;
    expresar ojos cerrados;
    expresar boca neutral;
    final
    """
    compiler_.compile(input_text)


if __name__ == "__main__":
    compiler = Compiler()
    example2(compiler)