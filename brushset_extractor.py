import os
import shutil

def copy_shape_png_files(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith('.png') and 'Shape' in file:
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(dst_folder, file)
                
                # Ensure we don't overwrite files with the same name
                base, extension = os.path.splitext(file)
                counter = 1
                while os.path.exists(dst_file_path):
                    new_file_name = f"{base}_{counter}{extension}"
                    dst_file_path = os.path.join(dst_folder, new_file_name)
                    counter += 1
                
                shutil.copy2(src_file_path, dst_file_path)
                print(f"Copied {src_file_path} to {dst_file_path}")

def main():
    base_folder = './in'  # Replace with the path to your base folder
    output_folder = './out'  # Replace with the path to your output folder
    
    sub_folders = ['folder_name']
    
    for subfolder in sub_folders:
        src_folder = os.path.join(base_folder, subfolder)
        dst_folder = os.path.join(output_folder, subfolder)
        copy_shape_png_files(src_folder, dst_folder)

if __name__ == '__main__':
    main()
