# datos = {
#     "a" :1,
#     "b" :2,
#     "c" :3,
#     "d" :4,
# }




# def dividir_chunks (diccionario, tamaño_chunck = 200, solape = 40):
#     items = list(diccionario.items ())
#     paso = tamaño_chunck - solape
#     return[dict(items[i:i+tamaño_chunck]) for i in range(0, len(items)-tamaño_chunck +1 , paso)]

#     # chunks = dividir_chuncks(datos, 3)
# resultado = dividir_chunks (datos, 3, 1)

# for i, chunk in enumerate(resultado):
#     print(f"Chunk {i+1}:", chunk)

def solapar_diccionario(diccionario, tamaño_chunk, solape):
    items = list(diccionario.items())  # [(1, 'texto1'), (2, 'texto2'), ...]
    paso = tamaño_chunk - solape

    chunks = []
    for i in range(0, len(items) - tamaño_chunk + 1, paso):
        pedazo = dict(items[i:i + tamaño_chunk])
        chunks.append(pedazo)

    return chunks
