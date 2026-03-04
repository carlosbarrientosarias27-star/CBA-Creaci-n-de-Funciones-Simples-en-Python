def validar_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
    
# Ejemplos de uso 
print(validar_email("usuario@ejemplo.com")) # True
print(validar_email("usuario.com")) # False