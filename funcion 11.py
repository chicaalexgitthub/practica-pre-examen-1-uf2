# Importamos los datos desde data
from data import *


# Declaracion de la funcion.
def order_dict_by_key(diccionario, orden, key=""):
    # Usamos try/except para revisar que todo sea correcto.
    try:
        # Si el parametro orden no es "des" o "asc" entramos en except como TypeError.
        if orden not in ("des", "asc"):
            raise TypeError("Invalid sort parameter.")
        # Como vamos a repetir bastante este codigo, lo guardamos en una variable.
        x = list(diccionario.keys())
        # Declaramos la lista en la que guardaremos el diccionario ordenado,
        res = []
        # Si el diccionario no esta formado por otro diccionario, entramos en este if.
        if type(diccionario[x[0]]) != dict:
            # En caso de que no se haya pasado un parametro key, entramps en except como TypeError.
            if key != "":
                raise TypeError("This dictionary doesn't support the key parameter.")
            # Iteramos para comprobar que todos los contenidos sean del mismo tipo.
            for i in range(1, len(x)):
                # En caso de que no sea todo del mismo tipo, entramos en except como TypeError.
                if type(diccionario[x[i]]) != type(diccionario[x[i - 1]]):
                    raise TypeError("All content from the dictionary must be of the same type")
            # Añadimos las keys del diccionario a la lista donde las vamos a ordenar.
            for i in x:
                res.append(i)
            # En caso de que el parametro orden sea "des", ordenamos de forma descendente mediante bubble sort.
            if orden == "des":
                for i in range(0, len(res)):
                    for j in range(0, len(res) - 1):
                        if diccionario[res[i]] > diccionario[res[j]]:
                            res[i], res[j] = res[j], res[i]
            # Ordenamos de forma ascendente mediante bubble sort.
            else:
                for i in range(0, len(res)):
                    for j in range(0, len(res) - 1):
                        if diccionario[res[i]] < diccionario[res[j]]:
                            res[i], res[j] = res[j], res[i]
            # Devolvemos la lista ordenada.
            return res
        # Si entramos aqui es porque el diccionario contiene otro diccionario.
        else:
            # Si no hay parametro key definido, entramos en except como TypeError.
            if key == "":
                raise TypeError("You must add a key parameter for this dictionary.")
            # si el parametro key no existe en el diccionario, entramos en except como TypeError.
            if key != "" and key not in diccionario[x[0]]:
                raise TypeError("Unable to find key parameter in the dictionary.")
            # Añadimos las keys del diccionario a la lista resultado.
            for i in x:
                res.append(i)
            # Ordenamos por bubble sort de forma descendente.
            if orden == "des":
                for i in range(0, len(res)):
                    for j in range(0, len(res) - 1):
                        if diccionario[res[i]][key] > diccionario[res[j]][key]:
                            res[i], res[j] = res[j], res[i]
            # Ordenamos por bubble sort de forma ascendente.
            else:
                for i in range(0, len(res)):
                    for j in range(0, len(res) - 1):
                        if diccionario[res[i]][key] < diccionario[res[j]][key]:
                            res[i], res[j] = res[j], res[i]
            # Devolvemos la lista ordenada.
            return res
    # En caso de TypeError, imprimimos el mensaje y salimos de la funcion.
    except TypeError as error:
        print(error)
        input("Press enter to continue.")
        return


k = order_dict_by_key({3: 5, 4: 4, 1: 5, 2: 2}, "des")
print(k)
