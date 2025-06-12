import re

def limpiar_texto(Archivo_pdf):
    # Aquí agrupamos todos los caracteres a eliminar dentro de un set `[]`
    pattern = r"[\n&_^~¢£¤¥¦§¨©ª«¬®¯±µ¶·¸¹º»×÷ʃʒʔʕʖ†‡•‣․‥…‰‱′″‴‵‶‷‹›※‼⁂⁎⁑⁕⁖⁘⁙⁚⁛⁜℅ℓ№℗℘ℙ℞℠™℣Ω℧℮⅍↔↕↖↗↘↙↩↪⇄⇅⇆⇇⇈⇉⇊⇋⇌⇍⇎⇏⇐⇑⇒⇓⇔∂∃∅∆∇∈∉∋∏∑∓∔∕√∝∞∟∠∡∢∣∤∥∦∧∨∩∪∫∬∭∮∯∰∴∵∶∷∸∹∺∻∼∽∾≀≁≂≃≄≅≆≇≈≉≊]"
    
    with open (Archivo_pdf, "r", encoding="utf-8") as f:
        texto=f.read()
    
    texto_limpio = re.sub(pattern, " ", texto)
    return texto_limpio
