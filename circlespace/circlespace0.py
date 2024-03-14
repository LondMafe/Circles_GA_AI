from PIL import Image, ImageDraw

# Tamaño de la imagen
width, height = 400, 400

# Crear una nueva imagen
image = Image.new("RGB", (width, height), "white")

# Crear un objeto para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Coordenadas y radio del círculo
x, y = width // 2, height // 2
radius = 100

# Dibujar el círculo
draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")

# Guardar la imagen
image.save("circle.png")

# Mostrar la imagen (opcional)
image.show()
