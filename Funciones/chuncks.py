# def chunk_palabras_solapado(diccionario, tamaño_chunk, solape):
#     # 1. Ordenar el diccionario por clave (número de página) y unir los textos
#     texto_total = " ".join(diccionario[k] for k in sorted(diccionario.keys()))
    
#     # 2. Dividir el texto completo en una lista de palabras
#     palabras = texto_total.split()
    
#     # 3. Crear los chunks solapados
#     paso = tamaño_chunk - solape
#     chunks = []
#     for i in range(0, len(palabras) - tamaño_chunk + 1, paso):
#         chunk = palabras[i:i + tamaño_chunk]
#         texto_chunk = " ".join(chunk)
#         chunks.append(texto_chunk)
#     for i, ch in enumerate(chunks, 1):
#         print(f"\n🔹 Chunk {i}:\n{ch}")

#     return chunks

def chunk_palabras_solapado(texto, largo, solapamiento):
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + largo
        chunk = texto[inicio:fin].strip()
        if len(chunk) > 50:  # evitar basura corta
            chunks.append(chunk)
        inicio += largo - solapamiento
    return chunks