import random
from math import sqrt
from PIL import Image, ImageDraw

# Size of the canvas
canvas_width, canvas_height = 1000, 800  # Lienzo rectangular

# Create a new image
image = Image.new("RGB", (canvas_width, canvas_height), "white")

# Create an object to draw on the image
draw = ImageDraw.Draw(image)

# List to store the data of the drawn circles
circles_data = []

# Number of circles to draw
num_circles = random.randint(10, 30)

# Draw multiple circles without overlap
for _ in range(num_circles):
    # Generate random coordinates and radius for the new circle
    x = random.randint(50, canvas_width - 50) # Ensure the circle is within the canvas
    y = random.randint(50, canvas_height - 50)  # Ensure the circle is within the canvas
    radius = random.randint(20, min(canvas_width, canvas_height) // 10) # Adjust the radius
    
    # Verify if there is a collision with the previously drawn circles
    collision = False
    for cx, cy, r in circles_data:
        distance = sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius + r:
            collision = True
            break
    
    # If there is no collision and the circle is within the canvas, draw it and add it to the list of drawn circles
    if not collision:
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline="black")
        circles_data.append([x, y, radius])

# Save the data of the circles in a text file
with open("circle_data.txt", "w") as file:
    for circle in circles_data:
        file.write(f"x: {circle[0]}, y: {circle[1]}, radius: {circle[2]}\n")

# Save the image
image.save("multiple_circles_no_overlap.png")

# Show the image
image.show()