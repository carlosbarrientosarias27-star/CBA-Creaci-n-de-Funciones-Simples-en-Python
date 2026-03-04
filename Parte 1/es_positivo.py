def es_positivo(numero):
    if numero > 0:
        return True
    else:
        return False

# Pruebas con varios valores
print(es_positivo(5))     # True
print(es_positivo(-3))    # False
print(es_positivo(0))     # False
print(es_positivo(2.5))   # True