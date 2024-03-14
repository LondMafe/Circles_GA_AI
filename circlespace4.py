import random
from math import sqrt
from PIL import Image, ImageDraw

# Tamaño del lienzo
canvas_width, canvas_height = 1000, 800  # Lienzo rectangular

# Crear una nueva imagen
image = Image.new("RGB", (canvas_width, canvas_height), "white")

# Crear un objeto para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Lista para almacenar los datos de los círculos dibujados
circles_data = []

# Número de círculos a dibujar
num_circles = random.randint(10, 30)

# Dibujar múltiples círculos sin superposición
for _ in range(num_circles):
    # Generar coordenadas y radio aleatorios para el nuevo círculo
    x = random.randint(50, canvas_width - 50)  # Asegurar que el círculo esté dentro del lienzo
    y = random.randint(50, canvas_height - 50)  # Asegurar que el círculo esté dentro del lienzo
    radius = random.randint(20, min(canvas_width, canvas_height) // 10)  # Ajustar el radio
    
    # Verificar si hay colisión con los círculos previamente dibujados
    collision = False
    for cx, cy, r in circles_data:
        distance = sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius + r:
            collision = True
            break
    
    # Si no hay colisión y el círculo está dentro del lienzo, dibujarlo y agregarlo a la lista de círculos dibujados
    if not collision:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")
        circles_data.append([x, y, radius])

# Guardar los datos de los círculos en un archivo de texto
with open("circle_data.txt", "w") as file:
    for circle in circles_data:
        file.write(f"x: {circle[0]}, y: {circle[1]}, radius: {circle[2]}\n")

# Guardar la imagen
image.save("multiple_circles_no_overlap.png")

# Mostrar la imagen (opcional)
image.show()
