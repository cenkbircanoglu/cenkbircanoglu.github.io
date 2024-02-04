from PIL import Image


def crop_right_percentage(image_path, percentage):
    original_image = Image.open(image_path)
    width, height = original_image.size

    crop_width = int(width * (1 - percentage / 100))

    cropped_image = original_image.crop((0, 0, crop_width, height))
    cropped_image.save("hero-bg.jpg")  # Save the cropped image with a new name

# Example usage
image_path = "hero-bg.jpg"
crop_percentage = 10
crop_right_percentage(image_path, crop_percentage)