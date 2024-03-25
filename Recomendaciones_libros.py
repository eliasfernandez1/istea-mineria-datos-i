# Tarea minería de datos clase 2

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)

lista_libros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]

def agregar_libro():
    titulo = str(input("Ingrese el título del libro: "))
    autor = str(input("Ingrese el autor del libro: "))
    genero = str(input("Ingrese el género del libro: "))
    puntuacion = float(input("Ingrese la puntuación del libro: "))
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)
    print("El libro se agregó correctamente")

def buscar_libros_por_genero():
    genero_busqueda = input("Ingrese el género que desea buscar: ")
    libros_en_genero = [libro.titulo for libro in lista_libros]
    if libros_en_genero:
        print("Libros en el género", genero_busqueda + ":")
        for titulo in libros_en_genero:
            print("- " + titulo)
    else:
        print(f"No se encontraron libros del género: {genero_busqueda}")

def obtener_puntuacion(libro):
    return libro.puntuacion

def recomendar_libro():
    genero_interes = str(input("Ingrese el género del libro: "))
    libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() in genero_interes.lower()]
    if libros_en_genero:
        libro_recomendado = max(libros_en_genero, key=obtener_puntuacion)
        print("El libro de mayor puntuación del género", genero_interes, "es: ")
        print("Título:", libro_recomendado.titulo)
        print("Autor:", libro_recomendado.autor)
        print("Puntuación:", libro_recomendado.puntuacion)
    else:
        print("Lo sentimos, no hay libros en el género:", genero_interes)

while True:
    print("1- Agregar libro")
    print("2- Buscar libros por género")
    print("3- Recomendar libro por género (Ficción, Ciencia Ficción, Fantasía, Romanse, Clásico, Juvenil, Histórica)")
    print("4- Salir")
    
    opcion = str(input("Seleccione una opción: "))
    
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        buscar_libros_por_genero()
    elif opcion == "3":
        recomendar_libro()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("¡ERROR! Por favor, seleccione una opción válida.")