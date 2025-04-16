import os
from PIL import Image, ImageOps

def invert_image(input_path, output_path):
    """
    Invert the colors of an image so that black becomes white and white becomes black.
    Saves the result as a new file.
    """
    try:
        img = Image.open(input_path)
    except Exception as e:
        print(f"Error opening {input_path}: {e}")
        return

    # If the image has an alpha channel, split it so we can invert RGB only.
    if img.mode == 'RGBA':
        r, g, b, a = img.split()
        rgb_inverted = ImageOps.invert(Image.merge('RGB', (r, g, b)))
        img_inverted = Image.merge('RGBA', (*rgb_inverted.split(), a))
    else:
        img_inverted = ImageOps.invert(img)

    try:
        img_inverted.save(output_path)
        print(f"Inverted image saved to: {output_path}")
    except Exception as e:
        print(f"Error saving {output_path}: {e}")

def process_folders(input_folder, output_folder, valid_extensions=('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
    """
    Processes each image file in the input folder by inverting it and saves the result in the output folder.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # Process each file in the input directory
    for filename in os.listdir(input_folder):
        # Check file extension to process only image files
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            print(f"Processing {input_path}...")
            invert_image(input_path, output_path)
        else:
            print(f"Skipping non-image file: {filename}")

def main():
    in_dir = 'in'
    out_dir = 'out2'

    process_folders(in_dir, out_dir)

if __name__ == "__main__":
    main()
