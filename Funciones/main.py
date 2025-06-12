"""
Este es el archivo principal con el cual se ejecutan todos los scripts sobre el pdf
que se obtiene de {ruta_pdf} y se guarda un archivo modificado en {guardar_en}
"""

from procesar import procesar_pdf

ruta_pdf = "data/Input/potter.pdf"

guardar_en = "data/Output"

procesar_pdf(ruta_pdf, guardar_en)