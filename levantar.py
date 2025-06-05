import PyPDF2
import fitz
try:
    documento_pdf = "documento.pdf"
    doc = fitz.open(documento_pdf)
    for numero_pagina, i in enumerate(range(len(doc)), start=1):
        
        pagina = doc.load_page(i)
        texto = pagina.get_text()
        print(f"--- Página {numero_pagina} ---")
        print(texto)
    doc.close()
except Exception as e:
    
    print("Fallo")
    with open("documento.pdf", "rb") as archivo:
        
        lector = PyPDF2.PdfReader(archivo)
        
    for numero_pagina, pagina in enumerate(lector.pages, start=1):
        
        texto = pagina.extract_text()
        print(f"--- Página {numero_pagina} ---")
        print(texto)
