from math import sqrt
import random

# Función para calcular el área de un círculo
def circle_area(radius):
    return 3.1416 * radius * radius

# Leer los datos de los círculos del archivo "circle_data.txt"
circles_data = []
with open("circle_data.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        x = int(data[0].split(":")[1])
        y = int(data[1].split(":")[1])
        radius = int(data[2].split(":")[1])
        circles_data.append((x, y, radius))

# Función de evaluación (fitness)
def evaluate(individual):
    # Verificar si hay colisiones
    for circle1 in individual:
        for circle2 in individual:
            if circle1 != circle2:
                distance = sqrt((circle1[0] - circle2[0])**2 + (circle1[1] - circle2[1])**2)
                if distance < circle1[2] + circle2[2]:
                    return 0  # Colisión, fitness = 0
    # Calcular el área del círculo más grande
    max_radius = max([circle[2] for circle in individual])
    return circle_area(max_radius)

# Algoritmo genético
def genetic_algorithm():
    # Inicialización de la población
    population = []
    for _ in range(10):  # Tamaño de la población
        individual = []
        for _ in range(random.randint(1, 5)):  # Número de círculos en cada individuo
            individual.append(random.choice(circles_data))
        population.append(individual)

    # Evaluación de la población inicial
    population_fitness = [(evaluate(individual), individual) for individual in population]
    population_fitness.sort(reverse=True)

    # Bucle de generaciones
    for generation in range(100):  # Número de generaciones
        # Selección
        selected = population_fitness[:5]  # Elitismo

        # Cruzamiento y mutación
        children = []
        for _ in range(5):  # Tamaño de la población - número de padres seleccionados
            parent1 = random.choice(population_fitness)[1]
            parent2 = random.choice(population_fitness)[1]
            child = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
            children.append(child)

        # Evaluación de los hijos
        children_fitness = [(evaluate(child), child) for child in children]

        # Reemplazo de la población
        population_fitness = selected + children_fitness
        population_fitness.sort(reverse=True)
        population = [individual for _, individual in population_fitness[:5]]

        # Imprimir el mejor individuo de cada generación
        print(f"Generación {generation+1}, Mejor fitness: {population_fitness[0][0]}")

    # Devolver el mejor individuo encontrado
    return population_fitness[0][1]

# Ejecutar el algoritmo genético
best_individual = genetic_algorithm()
print("Mejor individuo:", best_individual)
