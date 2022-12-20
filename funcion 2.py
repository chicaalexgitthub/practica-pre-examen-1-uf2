# Declaramos la funcion.
def new_tfn():
    # Ejecutamos dentro de try/except para revisar que los datos sean correcto.
    try:
        # Pedimos al usuario un telefono.
        tfn = input("Introduce the new tfn: ")
        # Si el telefono no esta formado unicamente por digitos, entramos en except como ValueError.
        if not tfn.isdigit():
            raise ValueError("The tfn must be all digits.")
        # Si la longitud del telefono no es 9, entramos en except como ValueError.
        elif not len(tfn) == 9:
            raise ValueError("The tfn must be 9 digits long.")
        # Devolvemos el nuevo telefono.
        return tfn
    # En caso de ValueError, printeamos el mensaje de error, y volvemos a llamar a la funcion.
    except ValueError as error:
        print(error)
        input("Press enter to continue.")
        new_tfn()


new_tfn()
