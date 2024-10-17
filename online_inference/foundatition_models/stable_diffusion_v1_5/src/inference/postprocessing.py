import os
from PIL import Image

def save_image(image, output_dir, file_name="generated_image.png"):
    """
    Saves the generated image to the specified directory.
    
    Args:
        image (PIL.Image): Generated image to be saved.
        output_dir (str): Path to the output directory.
        file_name (str): Name of the output file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_path = os.path.join(output_dir, file_name)
    image.save(file_path)
    print(f"Image saved to {file_path}")
