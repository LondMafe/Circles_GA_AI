import random
from math import sqrt
from PIL import Image, ImageDraw

# Tamaño del lienzo
canvas_width, canvas_height = 800, 800

# Crear una nueva imagen
image = Image.new("RGB", (canvas_width, canvas_height), "white")

# Crear un objeto para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Lista para almacenar las posiciones y radios de los círculos dibujados
circles = []

# Número de círculos a dibujar
num_circles = random.randint(10, 30)

# Dibujar múltiples círculos sin superposición
for _ in range(num_circles):
    # Generar coordenadas y radio aleatorios para el nuevo círculo
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    radius = random.randint(20, 80)
    
    # Verificar si hay colisión con los círculos previamente dibujados
    collision = False
    for cx, cy, r in circles:
        distance = sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius + r:
            collision = True
            break
    
    # Si no hay colisión, dibujar el círculo y agregarlo a la lista de círculos dibujados
    if not collision:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")
        circles.append((x, y, radius))

# Guardar la imagen
image.save("multiple_circles_no_overlap.png")

# Mostrar la imagen (opcional)
image.show()
