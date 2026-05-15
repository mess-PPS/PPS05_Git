import unicodedata

def normalizar(palabra):
    # Convertimos la palabra a minúsculas para evitar diferencias por mayúsculas
    palabra = palabra.lower()
    # Descomponemos caracteres con tilde (á -> a + tilde)
    palabra = unicodedata.normalize('NFD', palabra)
    # Eliminamos las tildes para poder ordenar alfabéticamente
    palabra = ''.join(c for c in palabra if unicodedata.category(c) != 'Mn')
    return palabra

def cadena_mas_larga(lista):
    # Si la lista está vacía devolvemos cadena vacía
    if not lista:
        return ""

    # Buscamos la longitud máxima
    max_longitud = 0
    for palabra in lista:
        if len(palabra) > max_longitud:
            max_longitud = len(palabra)

    # Recolectamos todas las palabras que tienen la longitud máxima
    palabras_largas = []
    for palabra in lista:
        if len(palabra) == max_longitud:
            palabras_largas.append(palabra)

    # Ordenamos las palabras más largas alfabéticamente y devolvemos la primera
    # Ignoramos mayus, minus, tildes y virgulilla para evitar el orden Unicode de Python
    palabras_largas.sort(key=normalizar)
    return palabras_largas[0]


def main():
    print("Programa que devuelve la cadena más larga.")
    print("Introduce 5 palabras:")

    palabras = []
    contador = 0
    while contador < 5:
        entrada = input(f"Palabra {contador + 1}: ")
        # quitamos espacios al principio/final por si el usuario introduce " hola "
        entrada = entrada.strip()
        # Permitimos cadena vacía o solo letras
        if entrada != "" and not entrada.isalpha():
            print("Error: solo se permiten letras o cadena vacía. Inténtalo de nuevo.")
            continue

        palabras.append(entrada)
        contador += 1

    # Llamamos a la función que hemos definido
    resultado = cadena_mas_larga(palabras)

    # Mostramos el resultado por pantalla
    print("\nResultado:")
    if resultado == "":
        print(" ")
    else:
        print("La palabra más larga es:", resultado)

if __name__ == "__main__":
    main()
