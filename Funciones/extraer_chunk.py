import re

def devolver_archivo(txt):
    with open(txt, 'r', encoding='utf-8') as f:
        texto=f.read()
    texto_content=re.split(r"---(\d+)---", texto)
    texto_paginas={}
    for i in range(1, len(texto_content), 2):
        resultado = texto_content[i+1].strip() #if tex else ""
        texto_paginas[int(texto_content[i])]= resultado  # Imprime el contenido de cada página
    return texto_paginas if texto_paginas else None  # Retorna el diccionario con los textos extraídos o None si está vacío
