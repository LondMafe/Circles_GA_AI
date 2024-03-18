# Description: Genetic algorithm to find the largest circle that does not collide with other circles
# Made by: LondMafe

import random
from math import sqrt
from PIL import Image, ImageDraw

# Canvas size
canvas_width, canvas_height = 1000, 800  # Rectangular canvas

# Read the data of the circles drawn from the file "circle_data.txt"
circles_data = []
with open("circle_data.txt", "r") as file:
    for line in file:
        data = line.strip().split(", ")
        x = int(data[0].split(": ")[1])
        y = int(data[1].split(": ")[1])
        radius = int(data[2].split(": ")[1])
        circles_data.append((x, y, radius))

# Function to verify if a circle collides with other circles
def check_collision(circle, other_circles):
    x, y, radius = circle
    for cx, cy, r in other_circles:
        distance = sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius + r:  # Allow circles to touch, but not overlap
            return True
    return False

# Function to evaluate the size of the circle at a specific point on the canvas
def evaluate_circle_size(x, y, radius, other_circles):
    test_circle = (x, y, radius)
    if not check_collision(test_circle, other_circles):
        return radius
    return 0

def genetic_algorithm(circles_data, canvas_width, canvas_height, population_size):
    max_radius = min(canvas_width, canvas_height) // 2

    # Initialize population with random circles
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

    # Create a new image
    image = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(image)

    # Draw existing circles
    for circle in circles_data:
        x, y, radius = circle
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")

    # Draw the new largest circle found by the genetic algorithm in Barbie pink
    x, y, radius = best_circle
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="#F22780", fill="#F22780")

    for i in range(10):
        image.save(f"genetic_algorithm_run_{population_size}.png" )
    
    # Show the image
    
    image.show()

    best_fitness = max(fitness_scores)
    best_index = fitness_scores.index(best_fitness)
    best_circle = population[best_index]
    return best_circle, best_fitness

# Ejecutar el algoritmo con diferentes tamaños de población
sizes = [1000, 2000]  # Por ejemplo, primero con una población de 1000 y luego con 2000
results = []
for size in sizes:
    best_circle, best_fitness = genetic_algorithm(circles_data, canvas_width, canvas_height, size)
    results.append((size, best_circle, best_fitness))

# Imprime los resultados para comparar
for size, circle, fitness in results:
    print(f"Population Size {size}: Best Circle = {circle}, Fitness = {fitness}")