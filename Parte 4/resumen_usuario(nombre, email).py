def resumen_usuario(nombre, email):
    # 1. Capitalizar el nombre
    nombre_capitalizado = nombre.capitalize()
    
    # 2. Validar el email usando la función anterior
    if validar_email(email):
        return f"Usuario: {nombre_capitalizado} — Email correcto"
    else:
        return f"Usuario: {nombre_capitalizado} — Email inválido"