"""
Este es el archivo principal con el cual se ejecutan todos los scripts sobre el pdf
que se obtiene de {ruta_pdf} y se guarda un archivo modificado en {guardar_en}
"""
from extraer_chunk import devolver_archivo
from procesar import procesar_pdf

#palabras = ["Universo", "antiguo"]

#ruta_pdf = "/home/nicotito/Documents/Practicas-2/Data/Input/potter.pdf"

#guardar_en = "/home/nicotito/Documents/Practicas-2/Data/Output/"

#procesar_pdf(ruta_pdf, guardar_en, palabras)

guardar_en = "/home/nicotito/Documents/Practicas-2/Data/Output/potter_texto.txt"

devolver_archivo(guardar_en)





