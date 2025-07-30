# What is scripting?
# Scripting is a way to automate tasks by writing small programs or scripts.
# It allows you to write code that can be executed to perform specific tasks, such as file manipulation, data processing, or system administration.
# Scripting languages are often interpreted rather than compiled, making them easier to write and run quickly.
# Scripting is commonly used in web development, system administration, and data analysis, among other fields.

# What is image processing?
# Image processing is the technique of manipulating and analyzing images using algorithms and software.
# It involves various operations such as filtering, transforming, and enhancing images to extract useful information or improve their quality.

from PIL import Image, ImageFilter

import os

print("Current working directory:", os.getcwd())

img_path = os.path.join(os.path.dirname(__file__), "fotos", "pikachu.jpg")
img = Image.open(img_path)

print(f"Image format: {img.mode}")
print(f"Image size: {img.size}")

save_path = os.path.join(os.path.dirname(
    __file__), "fotos", "pikachu_processed.png")

# The script opens an image, applies a blur filter, and saves the processed image. You can also use smaller filters like SHARPEN or CONTOUR. Smoothing is also available, but it is not as effective as the blur filter. You can also use the ImageEnhance module to adjust brightness, contrast, and color balance.


def process_image(image_path, output_path):
    try:
        # Open an image file
        with Image.open(image_path) as img:
            # Apply a filter to the image
            filtered_img = img.filter(ImageFilter.BLUR)
            # Save the processed image
            filtered_img.save(output_path)
            print(f"Image processed and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


process_image(img_path, save_path)

img_path2 = os.path.join(os.path.dirname(__file__), "fotos", "pikachu.jpg")
save_path2 = os.path.join(os.path.dirname(
    __file__), "fotos", "pikachu_converted.png")


def convert_image(image_path, output_path, format='PNG'):
    try:
        # Open an image file
        with Image.open(image_path) as img:
            # Convert and save the image in the specified format
            img.convert('L').save(output_path, format=format)
            print(
                f"Image converted and saved to {output_path} in {format} format")
    except Exception as e:
        print(f"An error occurred: {e}")


convert_image(img_path2, save_path2, format='PNG')
