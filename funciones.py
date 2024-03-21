def saludo(nombre):
    print(f'hola {nombre}')
saludo('tanya')
def nombre_edad(nombre, edad, estado_civil, altura):
    print(f'Hola soy {nombre} tengo {edad} años y soy {estado_civil} y mido {altura}')
nombre_edad('Tanya',46,'casada' ,165)

def fav_lenguaje(nombre,Python):
    print(f"Mi nombre es {nombre} y mi lenguaje de programación favorito es {'lenguaje'}!")
fav_lenguaje('Tanya', 'python')

def largo_palabra(frase):
    words = frase.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))
print(largo_palabra('Hola soy la mas guapa'))

def largo_palabra(frase):
    words = frase.split()
    lengths = {}
    for word in words:
        lengths[word] = len(word)
    return lengths

print(largo_palabra('Hola soy la mas guapa')) 





pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
         {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
         {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
         {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
         {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def precio_pisos(pisos):
    for piso in pisos:
        precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2024 - piso['año']) / 100)
        if piso['zona'] == 'B':
            precio *= 1.5
        piso['precio'] = precio
    return pisos

def busca_piso(pisos, presupuesto):
    pisos_disponibles = []
    for piso in precio_pisos(pisos):
        if piso['precio'] >= presupuesto:
            pisos_disponibles.append(piso)
    return pisos_disponibles

print(busca_piso(pisos, 80000))




