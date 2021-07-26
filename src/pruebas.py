"""
print("Hola Mundo!! Soy Jimmy Hawkins TechDrivePTY :)")
print("Hola Mundo!! 2")
print("Hola Mundo!! 3")
"""

# Soy un comentario
# print("Hola Mundo 4")

"""
Texto que no va a interpretar
Texto que no va a interpretar
Texto que no va a interpretar
"""
# Variables
texto = "Aprendiendo python con Victor"
nombre = "Jimmy Hawkins"
Altura = "187cm"
year = 2020

"""
print(f"{texto} - {nombre} - {Altura} - {str(year)}")
print(texto + " - " + nombre + " - " + Altura + " - " + str(year))
"""
# Entrada
# sitioweb = input("¿Cuál es tu página web?: ")
# print(f"El sitio web del usuario es: {sitioweb}")
# print("El sitio web del usuario es: " + sitioweb)

# Condiciones
"""
altura = int(input("¿Cuál es tu altura?: "))

if altura >= 180:
    print("Eres una persona alta!!")
else:
    print("Eres bajito")
"""

# Funciones
"""
var_altura = int(input("¿Cuál es tu altura?: "))
def mostrarAltura(altura):
    resultado = ""
    if altura >= 180:
        resultado = "Eres una persona alta!!"
    else:
        resultado = "Eres BAJITO!!"
    
    return resultado

print(mostrarAltura(var_altura))
"""

# Listas
personas = [
    {"nombre": "Jimmy", "apellido": "Hawkins"},
    {"nombre": "Jason", "apellido": "Arenas"},
    {"nombre": "Allyson", "apellido": "Castillo"}
]
# print(personas[2])

for persona in personas:
    print("-" + persona["nombre"] + ", " + persona["apellido"])
