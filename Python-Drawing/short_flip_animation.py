# This program creates short flipbook animation
import pygame
import math
import os
from PIL import Image


def count_images_in_directory(directory):
    image_count = 0
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            image_count += 1
            # Optionally, you can open the image to verify it's valid
            try:
                img = Image.open(os.path.join(directory, filename))
                img.verify()  # This checks if the image is valid
            except (IOError, SyntaxError):
                print(f"File {filename} is not a valid image.")
    return image_count


# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Short Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load images
images = []
images_count = count_images_in_directory("Images")
for i in range(1, images_count + 1):
    img_path = os.path.join("Images", f"image-{i}.png")
    if os.path.exists(img_path):
        img = pygame.image.load(img_path).convert_alpha()
        images.append(pygame.transform.scale(img, (300, 450)))  # Image size
    else:
        print(f"Image not found: {img_path}")  # Debugging line

if not images:
    print("No images were loaded. Exiting.")
    pygame.quit()
    exit()  # Or handle it in another way

# Define position and attributes
coor_x = width // 2
coor_y = height // 2
frame_index = 0

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle animation frame update
    frame_index += 1
    if frame_index >= len(images):
        frame_index = 0

    # Draw animation
    image = images[frame_index]
    screen.blit(image, (coor_x - image.get_width() // 2, coor_y - image.get_height() // 2))

    pygame.display.flip()
    clock.tick(2)  # Adjust animation speed as needed

pygame.quit()
