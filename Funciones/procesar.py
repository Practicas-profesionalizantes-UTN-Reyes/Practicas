from levantar import levantar_pdf
from extraerimg import TierniFun
import os

def procesar_pdf(path_pdf, guardar):
    texto = levantar_pdf(path_pdf)
    
    if texto is None or all(t.strip() == "" for t in texto.values()):
        print("PDF sin texto, usando el OCR")
        texto = TierniFun(path_pdf)
    
    if texto:
        nombre_archivo_pdf = os.path.splitext(os.path.basename(path_pdf))[0]
        output_path = os.path.join(guardar, f"{nombre_archivo_pdf}_texto.txt")
        with open (output_path, "w", encoding="utf-8") as f:
            for pagina, contenido in texto.items():
                f.write(f"---{pagina}---\n")
                f.write(f"{contenido}\n\n")
        print(f"Texto guardado en {output_path}")
    else:
        print("Sin contenido")                  
