from extraer_chunk import devolver_archivo
from chuncks import chunk_palabras_solapado

def hacer_json(direccion_txt):
    diccionario = devolver_archivo(direccion_txt)
    diccionario_1 = chunk_palabras_solapado(diccionario ,100,10)
    
 