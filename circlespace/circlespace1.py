import random
from PIL import Image, ImageDraw

# Tamaño del lienzo
canvas_width, canvas_height = 800, 800

# Crear una nueva imagen
image = Image.new("RGB", (canvas_width, canvas_height), "white")

# Crear un objeto para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Número de círculos a dibujar
num_circles = random.randint(10, 30)

# Dibujar múltiples círculos
for _ in range(num_circles):
    # Coordenadas y radio del círculo
    x = random.randint(0, canvas_width)
    y = random.randint(0, canvas_height)
    radius = random.randint(20, 80)
    
    # Dibujar el círculo
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")

# Guardar la imagen
image.save("multiple_circles.png")

# Mostrar la imagen (opcional)
image.show()