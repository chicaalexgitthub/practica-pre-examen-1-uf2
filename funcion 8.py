# Declaracion de la funcion.
def find_item_id():
    # Ejecutamos la funcion controlando posibles errores.
    try:
        # Pedimos la id deseada y la guardamos.
        search = input("ID of the item: ")
        # En caso de que la id no sea digito exploramos dos opciones.
        if not search.isdigit():
            # Si la opcion empieza por '-' y el resto son digitos, es decimal, alzamos el error correspondente.
            if search[0] == "-" and search[1:].isdigit():
                raise ValueError("The ID must be positive.")
            # Si no es decimal, alzamos el error de que no es digito.
            raise ValueError("The ID must be a digit.")
        # Comprobamos que la id este en el diccionario de articulos.
        if not int(search) in dict_articulos:
            # Si la id no existe alzamos el error correspondiente.
            raise ValueError("The ID doesn't exist.")
        # La id es correcta asi que la devolvemos.
        return search
    # En caso de error lo imprimos y volvemos a llamar a la funcion.
    except ValueError as error:
        print(error)
        input("Press enter to continue.")
        find_item_id()


dict_articulos = { 4: { "nombre": "ASUS TUF GeForce RT X", "stock": 6, "precio": 1400} ,
2: { "nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294} ,
3: { "nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530} ,
1: { "nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
10: { "nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110},
11: { "nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81} ,
}
find_item_id()
