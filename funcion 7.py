# Definimos la funcion sin paramatros.
def new_item_name():
    try:
        # Pedimos el nombre del articulo.
        product_name = input("Introduce the item's name: ")
        # Iteramos los diferentes nombres de articulo en busca de si coincide con alguno.
        for item in dict_articulos:
            if product_name.lower() == dict_articulos[item]["nombre"].lower():
                # Alzamos un ValueError ya que el nombre ya existe.
                raise ValueError("The item name already exists.")
        # Comprobamos que el nombre no sean espacios o este vacio.
        if product_name.isspace() or product_name == "":
            # Alamos un ValueError ya que el nombre esta vacio o es espacio.
            raise ValueError("The name cant be empty")
        # Devolvemos el nombre
        return product_name
    # En caso de ValueError, guardamos el mensaje de error como 'error'
    except ValueError as error:
        # Mostramos el mensaje por pantalla.
        print(error)
        input("Press enter to continue.")
        # Volvemos al principio de la funcion.
        new_item_name()


dict_articulos = {4: {"nombre": "ASUS TUF GeForce RT X", "stock": 6, "precio": 1400},
                  2: {"nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294},
                  3: {"nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530},
                  1: {"nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
                  10: {"nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110},
                  11: {"nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81},
                  }

name = new_item_name()
