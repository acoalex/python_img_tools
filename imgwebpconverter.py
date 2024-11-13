import os
import argparse
from PIL import Image

def convert_to_webp(path, quality):
    # Common image extensions to look for
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']

    # Recursively walk through all files in the given path
    for root, _, files in os.walk(path):
        for file in files:
            # Check if the file has an image extension
            if any(file.lower().endswith(ext) for ext in image_extensions):
                # Full path of the image file
                image_path = os.path.join(root, file)

                # Open the image and convert it to WebP
                with Image.open(image_path) as img:
                    # Define the destination path with .webp extension
                    webp_path = os.path.splitext(image_path)[0] + '.webp'
                    if os.path.exists(webp_path):
                        print(f'Skipping {image_path}, WebP version already exists.')
                        continue  # Skip to the next file 

                    try:
                        # Save the image in WebP format with the specified quality
                        img.save(webp_path, 'webp', quality=quality)
                        os.remove(image_path)
                    except Exception as e:
                        print(f'Error converting {image_path} to WebP: {e}')
                        continue

                print(f'Converted: {image_path} -> {webp_path}')

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Convert images to WebP format with a specified quality.")
    parser.add_argument('path', type=str, help="Absolute path to the directory containing images.")
    parser.add_argument('quality', type=int, help="Quality of the output WebP images (0-100).")

    # Parse the arguments
    args = parser.parse_args()

    # Call the conversion function with provided arguments
    convert_to_webp(args.path, args.quality)

