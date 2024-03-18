# Genetic Algorithm Biggest Circle Generator

**Circle Space:** Creates a canvas with a random amount of circles between 10-30, the coordinates and radius of the circles are also randomly generated. This canvas with circles is saved as a PNG file. The code also saves the info about each circle on a TXT file, that will later be read by the gen archive.

**Gen:** Uses a genetic algorith to fit the biggest circle possible in the blank spaces of the canvas without colliding with the other circles.

*Note:* The archives in the folders "circlespace" and "gen" are just the previous versions, the final files are *"circlespace4"* and *"gen5"*.

## Algoritmos Geneticos

Para el problema siguiente, haga:

1. Codifique un GA simple para resolver el problema. Para hacer esto, necesita codificar el problema, usar un cruce de un solo punto y un cambio de bits o una mutación de 2 opciones, usar una forma de selección de ruleta o selección de torneo, establecer un tamaño de población y seleccionar un criterio de parada.

2. Ejecute su GA.

3. Realice los siguientes cambios en su código GA (uno por uno) y compare el resultados.

    - Cambiar los puntos de partida iniciales (soluciones iniciales) diez veces

        - Run 1: Best Circle = (376, 358, 115), Fitness = 115![1](assets/genetic_algorithm_run_0.png)
        - Run 2: Best Circle = (358, 380, 126), Fitness = 126![2](assets/genetic_algorithm_run_1.png)
        - Run 3: Best Circle = (380, 394, 125), Fitness = 125![3](assets/genetic_algorithm_run_2.png)
        - Run 4: Best Circle = (356, 381, 126), Fitness = 126![4](assets/genetic_algorithm_run_3.png)
        - Run 5: Best Circle = (365, 390, 123), Fitness = 123![5](assets/genetic_algorithm_run_4.png)
        - Run 6: Best Circle = (366, 381, 131), Fitness = 131![6](assets/genetic_algorithm_run_5.png)
        - Run 7: Best Circle = (347, 379, 121), Fitness = 121![7](assets/genetic_algorithm_run_6.png)
        - Run 8: Best Circle = (367, 393, 121), Fitness = 121![8](assets/genetic_algorithm_run_7.png)
        - Run 9: Best Circle = (377, 380, 129), Fitness = 129![9](assets/genetic_algorithm_run_8.png)
        - Run 10: Best Circle = (354, 382, 127), Fitness = 127![10](assets/genetic_algorithm_run_9.png)

    - Cambiar la probabilidad de cruce dos veces
        - Crossover Probability 0.7: Best Circle = (691, 685, 115), Fitness = 115 ![11](assets/genetic_algorithm_run_0_cambiar.png)
        - Crossover Probability 0.9: Best Circle = (349, 385, 123), Fitness = 123 ![12](assets/genetic_algorithm_run_1_cambiar.png)

    - Cambiar la probabilidad de mutación dos veces
        - Mutation Probability 0.05: Best Circle = (376, 390, 127), Fitness = 127 ![13](assets/genetic_algorithm_run_0.05.png)
        - Mutation Probability 0.2: Best Circle = (367, 374, 125), Fitness = 125 ![14](assets/genetic_algorithm_run_0.2.png)
  
    - Cambiar el tamaño de la población dos veces
        - Population Size 1000: Best Circle = (370, 387, 128), Fitness = 128 ![15](assets/genetic_algorithm_run_1000.png)
        - Population Size 2000: Best Circle = (359, 379, 126), Fitness = 126 ![16](assets/genetic_algorithm_run_2000.png)

    - Cambie la semilla del número aleatorio diez veces
        - Random Seed 0: Best Circle = (376, 358, 115), Fitness = 115 ![17](assets/genetic_algorithm_run_seed_0.png)
        - Random Seed 1: Best Circle = (358, 380, 126), Fitness = 126 ![18](assets/genetic_algorithm_run_seed_1.png)
        - Random Seed 2: Best Circle = (380, 394, 125), Fitness = 125 ![19](assets/genetic_algorithm_run_seed_2.png)
        - Random Seed 3: Best Circle = (356, 381, 126), Fitness = 126 ![20](assets/genetic_algorithm_run_seed_3.png)
        - Random Seed 4: Best Circle = (365, 390, 123), Fitness = 123 ![21](assets/genetic_algorithm_run_seed_4.png)
        - Random Seed 5: Best Circle = (366, 381, 131), Fitness = 131 ![22](assets/genetic_algorithm_run_seed_5.png)
        - Random Seed 6: Best Circle = (347, 379, 121), Fitness = 121 ![23](assets/genetic_algorithm_run_seed_6.png)
        - Random Seed 7: Best Circle = (367, 393, 121), Fitness = 121 ![24](assets/genetic_algorithm_run_seed_7.png)
        - Random Seed 8: Best Circle = (377, 380, 129), Fitness = 129 ![25](assets/genetic_algorithm_run_seed_8.png)
        - Random Seed 9: Best Circle = (354, 382, 127), Fitness = 127 ![26](assets/genetic_algorithm_run_seed_9.png)
  
4. Incluya su código con su tarea.

5. Indique que el porcentaje de cada miembro del equipo contribuye a este asignación (solo si trabaja con otros).

6. No copie el trabajo de otro equipo/individuo. Cualquiera/cualquier equipo que viole este reglamento recibirá una calificación de cero para este taller.
Incluyo el óptimo global para cada problema como referencia, pero no lo use en su metodología de solución.

## Problema

Dada un área que tiene una cantidad de discos que no se superponen esparcidos por su superficie, como se muestra en la figura 1,

Utilice un algoritmo genético para encontrar el disco de mayor radio que se puede colocar entre estos discos sin superponer ninguno de ellos.  Ver figura 2.
