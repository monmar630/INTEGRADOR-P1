class Receta:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria
    
    def __str__(self):
        return f"{self.nombre} - {self.categoria}"
        

def ordenar_recetas(recetas):
    recetas.sort(key=lambda x: x.nombre)
    return recetas

def buscar_recetas(recetas, palabra_clave):
    resultados = [receta for receta in recetas if palabra_clave.lower() in receta.nombre.lower()]
    return resultados

#Ejemplo de uso
recetas = [Receta("Lasgna de espinaca", "Pastas"),
           Receta("Lomo a la pimienta", "Carnes"),
           Receta("Fideos al pesto", "Pastas"),
           Receta("Tarta de verduras", "Tartas"),
           Receta("Sorrentinos de ricota y espinaca", "Pastas"),
           Receta("Pollo con salteado de verduras", "Aves"),
           ]

#Ordenar recetas
recetas_ordenadas = ordenar_recetas(recetas)
print("Recetas ordenadas: ")
for receta in recetas_ordenadas:
    print(receta.nombre)

#Buscar recetas
palabra_clave = "espinaca"
resultados = buscar_recetas(recetas, palabra_clave)

if resultados:
    print(f"\nRecetas que contienen '{palabra_clave}':")
    for receta in resultados:
        print(receta.nombre)
else:
    print(f"\nNo se encontraron recetas que contengan '{palabra_clave}'")




