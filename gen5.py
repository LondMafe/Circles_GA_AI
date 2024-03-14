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
        if distance < radius + r:  # Permitir que los círculos se toquen, pero no se solapen
            return True
    return False

# Función para evaluar el tamaño del círculo en un punto específico del lienzo
def evaluate_circle_size(x, y, radius, other_circles):
    test_circle = (x, y, radius)
    if not check_collision(test_circle, other_circles):
        return radius
    return 0

def genetic_algorithm(circles_data, canvas_width, canvas_height):
    max_radius = min(canvas_width, canvas_height) // 2

    # Initialize population with random circles
    population_size = 1500
    population = [(random.randint(0, canvas_width), random.randint(0, canvas_height), random.randint(1, max_radius)) for _ in range(population_size)]

    # Fitness function: Evaluate circle size without collisions
    def fitness(circle):
        x, y, radius = circle
        if x - radius < 0 or x + radius > canvas_width or y - radius < 0 or y + radius > canvas_height:
            return 0  # Out of bounds
        return evaluate_circle_size(x, y, radius, circles_data)

    generations = 900
    for generation in range(generations):
        # Evaluate fitness
        fitness_scores = [fitness(circle) for circle in population]

        # Selection: Choose top performers as parents
        parents_indices = sorted(range(len(population)), key=lambda i: fitness_scores[i], reverse=True)[:population_size//2]
        parents = [population[i] for i in parents_indices]

        # Crossover: Produce offspring from pairs of parents
        offspring = []
        while len(offspring) < population_size - len(parents):
            parent1, parent2 = random.sample(parents, 2)
            child_x = (parent1[0] + parent2[0]) // 2
            child_y = (parent1[1] + parent2[1]) // 2
            child_radius = min((parent1[2] + parent2[2]) // 2, max_radius)
            offspring.append((child_x, child_y, child_radius))

        # Mutation: Slightly modify some offspring
        for i in range(len(offspring)):
            if random.random() < 0.1:  # Mutation probability
                mutate_radius = offspring[i][2] + random.randint(-2, 2)
                offspring[i] = (offspring[i][0], offspring[i][1], max(1, min(mutate_radius, max_radius)))

        # Form new generation
        population = parents + offspring

    # Find the best circle from the last generation
    best_fitness = max(fitness_scores)
    best_index = fitness_scores.index(best_fitness)
    best_circle = population[best_index]


    # Crear una nueva imagen
    image = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(image)

    # Dibujar los círculos existentes
    for circle in circles_data:
        x, y, radius = circle
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")

    # Dibujar el nuevo círculo más grande encontrado por el algoritmo genético en color rosa
    x, y, radius = best_circle
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="#F7238A", fill="#F7238A")

    # Guardar la imagen
    image.save("largest_circle.png")
    
    # Mostrar la imagen (opcional)
    image.show()

    return best_circle

# Ejecutar el algoritmo genético
best_circle = genetic_algorithm(circles_data, canvas_width, canvas_height)
