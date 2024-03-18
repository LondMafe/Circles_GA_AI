import random

def genetic_algorithm(circles_data, canvas_width, canvas_height, random_seed):
    random.seed(random_seed)  # Establece la semilla aleatoria

    
    best_fitness = max(fitness_scores)
    best_index = fitness_scores.index(best_fitness)
    best_circle = population[best_index]
    return best_circle, best_fitness

# Ejecutar el algoritmo 10 veces con diferentes semillas aleatorias
results = []
for seed in range(10):  # Usar un rango de 0 a 9 como semillas
    best_circle, best_fitness = genetic_algorithm(circles_data, canvas_width, canvas_height, seed)
    results.append((seed, best_circle, best_fitness))

# Comparar los resultados
for seed, circle, fitness in results:
    print(f"Random Seed {seed}: Best Circle = {circle}, Fitness = {fitness}")