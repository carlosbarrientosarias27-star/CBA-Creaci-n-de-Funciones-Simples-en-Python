import re

def validar_email(email):
    """
    Valida si el email tiene una estructura básica correcta.
    """
    if "@" in email and "." in email:
        return True
    else:
        return False

def resumen_usuario(nombre, email):
    """
    Capitaliza el nombre y valida el email.
    Devuelve un mensaje según la validez del correo.
    """
    # Capitalizar nombre (mejor que capitalize para nombres compuestos)
    nombre_capitalizado = nombre.title()
    
    # Validar email
    if validar_email(email):
        return f"Usuario: {nombre_capitalizado} — Email correcto"
    else:
        return f"Usuario: {nombre_capitalizado} — Email inválido"


# 🔎 Ejemplos de uso
print(resumen_usuario("juan perez", "juan@correo.com"))
print(resumen_usuario("maria", "mariacorreo.com"))