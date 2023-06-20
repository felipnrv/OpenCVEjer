frase = input("Decime una frase: ")
palabras_separadas = frase.split(" ")
cantidad_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras/2}")
print(f"Dalto lo diria en {round(1.3 * cantidad_palabras/2 - cantidad_palabras/2)} segundos en decirlo")



