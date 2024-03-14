import random
from math import sqrt
from PIL import Image, ImageDraw

# Tamaño del lienzo
canvas_width, canvas_height = 1000, 800  # Lienzo rectangular

# Leer los datos de los círculos dibujados desde el archivo "circle_data.txt"
circles_data = []
with open("circle_data.txt", "r") as file:
    for line in file:
        data = line.strip().split(", ")
        x = int(data[0].split(": ")[1])
        y = int(data[1].split(": ")[1])
        radius = int(data[2].split(": ")[1])
        circles_data.append((x, y, radius))

# Función para verificar si un círculo colisiona con otros círculos
def check_collision(circle, other_circles):
    x, y, radius = circle
    for cx, cy, r in other_circles:
        distance = sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius + r:
            return True
    return False

# Función para evaluar el tamaño del círculo en un punto específico del lienzo
def evaluate_circle_size(x, y, radius, other_circles):
    test_circle = (x, y, radius)
    if not check_collision(test_circle, other_circles):
        return radius
    return 0

# Algoritmo genético para encontrar el círculo más grande posible sin colisiones
def genetic_algorithm(circles_data, canvas_width, canvas_height):
    best_circle = (0, 0, 0)
    max_radius = min(canvas_width, canvas_height) // 2  # El radio máximo posible
    population_size = 100  # Tamaño de la población
    generations = 100  # Número de generaciones

    for _ in range(generations):
        population = [(random.randint(0, canvas_width), random.randint(0, canvas_height), random.randint(1, max_radius)) for _ in range(population_size)]
        
        for circle in population:
            x, y, radius = circle
            if x - radius < 0 or x + radius > canvas_width or y - radius < 0 or y + radius > canvas_height:
                continue  # Ignorar círculos que están fuera de los límites del lienzo

            if not check_collision(circle, circles_data):
                if radius > best_circle[2]:
                    best_circle = (x, y, radius)

    return best_circle

# Ejecutar el algoritmo genético
best_circle = genetic_algorithm(circles_data, canvas_width, canvas_height)

# Crear una nueva imagen
image = Image.new("RGB", (canvas_width, canvas_height), "white")

# Crear un objeto para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Dibujar los círculos existentes
for circle in circles_data:
    x, y, radius = circle
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")

# Dibujar el nuevo círculo más grande encontrado por el algoritmo genético en color rosa
x, y, radius = best_circle
draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="pink", fill="pink")

# Guardar la imagen
image.save("largest_circle.png")

# Mostrar la imagen (opcional)
image.show()
