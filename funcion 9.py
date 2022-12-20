# Declaramos la funcion.
def print_item(id, **values):
    # Imprimimos la id formateada hacia la derecha.
    print("ID".ljust(10), str(id).rjust(30))
    # Recorremos las diferents keys del diccionario.
    for key in dict_articulos[id]:
        # En caso de que una key coincida con "values" imprimos dicha key con el valor de "values".
        if key in values.keys():
            print(key.ljust(10), values[key].rjust(30))
        # Imprimimos los datos de queda key.
        else:
            print(key.ljust(10), str(dict_articulos[id][key]).rjust(30))


dict_articulos = {4: {"nombre": "ASUS TUF GeForce RT X", "stock": 6, "precio": 1400},
                  2: {"nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294},
                  3: {"nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530},
                  1: {"nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
                  10: {"nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110},
                  11: {"nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81},
                  }
print_item(2)

