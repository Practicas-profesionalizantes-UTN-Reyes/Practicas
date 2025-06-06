import PyPDF2
import fitz

def levantar_pdf(path):
    texto_paginas = {}

    try:
        doc = fitz.open(path)
        for numero_pagina in range(len(doc)):
            pagina = doc.load_page(numero_pagina)
            texto = pagina.get_text()
            texto_paginas[numero_pagina + 1] = texto.strip()
            print(f"--- Página {numero_pagina + 1} ---")
            print(texto)
        doc.close()
    except Exception as e:
        print("Fallo")
        with open(path, "rb") as archivo:
            lector = PyPDF2.PdfReader(archivo)
            for numero_pagina, pagina in enumerate(lector.pages, start=1):
                texto = pagina.extract_text()
                texto_paginas[numero_pagina] = texto.strip() if texto else ""
                print(f"--- Página {numero_pagina} ---")
                print(texto)

    return texto_paginas if texto_paginas else None
