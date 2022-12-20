# Declaracion de la funcion.
def getOpt(textOpts, inputOptText, lista, exceptions):
    # Ejecutamos la funcion mientras no se den errores.
    try:
        # Imprimimos el menu que hemos pasado a la funcion.
        print(textOpts)
        # Pedimos al usuario que introduzca una opcion.
        opt = input(inputOptText)

        # A continuacion vamos a identificar si opt introducida es valido.

        # En caso de que opt no este formada unicamente por digitos, entramos en este if.
        if not opt.isdigit():
            # Miramos si opt esta en exceptions.
            if opt in exceptions:
                # Devolvemos opt
                return opt
            # Comprobamos si opt empieza por '-' (posible negativo)
            elif opt[0] == "-" and opt[1:].isdigit():
                # Miramos si el resto de posiciones de opt son digitos, i si el negativo de dicho numero esta en
                # lista o exceptions.
                if - int(opt[1:]) in exceptions or - int(opt[1:]) in lista:
                    # Devolvemos opt
                    return opt
            # Si hemos llegado hasta aqui es porque la opcion no es valida, alzamos un typeError de error con un
            # mensaje.
            raise TypeError("Invalid Option. ")
        # Ya sabemos que opt es digito, asi que miramos si se encuentra en lista o exceptions.
        elif int(opt) in exceptions or int(opt) in lista:
            # Devolvemos opt
            return opt
        # Si llegamos aqui es porque se trata de error. Alzamos un typeError con un mensaje.
        raise TypeError("Invalid Option. ")
    # En caso de error (solo puede ser typeError), entramos en except y le asignamos el mensaje a la variable error.
    except TypeError as error:
        # Imprimimos el mensaje de error.
        print(error)
        input("Press enter to continue.")
        # Volvemos a llamar a la funcion desde el principio.
        getOpt(textOpts, inputOptText, lista, exceptions)


# Valores de prueba para las variables.
textOpts = "\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
inputOptText = "\nElige tu opción: "
lista = [1, 2, 3, 4]
exceptions = ["w", "e", -1]
# Llamamos a la funcion como valor de opc.
opc = getOpt(textOpts, inputOptText, lista, exceptions)
