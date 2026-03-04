def capitalizar(texto):
    if not texto:
        return "Texto vacío"
    return texto.title() 


# Ejemplos de uso
print(capitalizar("hola mundo"))  
# Resultado: Hola Mundo

print(capitalizar(""))  
# Resultado: Texto vacío