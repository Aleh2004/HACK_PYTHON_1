"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result_A = result.upper().replace('O', '0').replace('I', '1').replace('A', '@')
    # Convertir la cadena modificada en una lista de caracteres
    result = list(result_A)

    return result  