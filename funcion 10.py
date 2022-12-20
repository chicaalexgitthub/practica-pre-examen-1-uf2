# Declaracion de la funcion.
def order_list(llista, ordre="des"):
    # Usamos Try para detectar posibles errores.
    try:
        # Si "llista" no es de tipo "list" alzamos un ValueError
        if not type(llista) == list:
            raise ValueError("The parameter isn't a list.")
        # Si "ordre" no esta entre los valores definidos, alzamos ValueError.
        if ordre not in ("des", "asc"):
            raise ValueError("Invalid sort parameter.")
        # Iteramos las posiciones de "llista" para comprobar que sean del mismo tipo.
        for i in range(1, len(llista)):
            if type(llista[i]) != type(llista[i - 1]):
                raise TypeError("All list items must be of the same type.")
    # Si hay ValueError mostramos un mensaje y salimos de la funcion.
    except ValueError as error:
        print(error)
        input("Prees enter to continue.")
        return
    # Si hay TypeError mostramos un mensaje y salimos de la funcion.
    except TypeError as error:
        print(error)
        input("Prees enter to continue.")
        return
    # En caso de que ordre = "des", ordenamos descendentemente usado bubble sort.
    if ordre == "des":
        for i in range(0, len(llista)):
            for j in range(0, len(llista) - 1):
                if llista[i] > llista[j]:
                    llista[i], llista[j] = llista[j], llista[i]
    # En caso de que ordre = "asc", ordenamos ascendentemente usado bubble sort.
    else:
        for i in range(0, len(llista)):
            for j in range(0, len(llista) - 1):
                if llista[i] < llista[j]:
                    llista[i], llista[j] = llista[j], llista[i]
    # Devolvemos la lista ya ordenada.
    return llista


x = order_list([1, 6, 3, 2, 0, 5])
print(x)
