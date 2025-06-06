import pytesseract
from pdf2image import convert_from_path

def TierniFun(RutaArchivo):

    Imagen_Dic={}

    imagenes=convert_from_path(RutaArchivo)
    for i,imagen in enumerate(imagenes):
        text_img= pytesseract.image_to_string(imagen)
        Imagen_Dic[i+1] = text_img.strip()
    return Imagen_Dic
    
