import os
import shutil
from PIL import Image

# Define the path of the folder to be organized
path = r'\...'

# Mapping of file extensions to categories
file_categories = {
    'Code': {'html', 'css', 'js', 'py', 'cs', 'java'},
    'Images': {'jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'},
    'Videos': {'mp4', 'mkv', 'webm'},
    'Audio': {'mp3'},
    'Documents': {'pdf', 'docx', 'txt'},
    # Add other file extensions and their categories here
}

# Function to get the category of a file
def get_category(file_extension):
    for category, extensions in file_categories.items():
        if file_extension.lower() in extensions:
            return category
    return 'Other'

# Function to check if an image is HD (1080p)
def is_hd(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return width >= 2560 and height >= 1440
    
# Function to check if a video is more than 1GB
def is_larger_than_1GB(path):
    file_size = os.path.getsize(path)
    return file_size > (1024 * 1024 * 1024)  # Size in bytes

# List all files in the directory
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

for file in files:
    # Extract the file extension
    file_extension = file.split('.')[-1] if '.' in file else 'Other'
    # Determine the category of the file
    category = get_category(file_extension)
    # Define the source path of the file
    src_path = os.path.join(path, file)

    ## Organize into the Wallpaper folder
    # Check if the file is categorized as an image
    if category == 'Images':
        try:
            # If the file is an image, check if it's HD
            if is_hd(src_path):
                # Define the path for the Wallpapers folder
                wallpaper_folder = os.path.join(path, 'Wallpapers')
                # Create the Wallpapers folder if it doesn't exist
                if not os.path.exists(wallpaper_folder):
                    os.makedirs(wallpaper_folder)

                # Define the destination path for the HD image
                dest_path = os.path.join(wallpaper_folder, file)
                # Move the HD image to the Wallpapers folder
                shutil.move(src_path, dest_path)
                print(f'Moved HD image {file} to {dest_path}')
            else:
                # Here you can handle non-HD images if needed
                pass
        except Exception as e:
            # Print an error message if something goes wrong
            print(f'Error processing {file}: {e}')
    else:
        # Handle files that are not categorized as images
        pass



    # Construct the category and subfolder paths
    category_folder = os.path.join(path, category)
    subfolder_path = os.path.join(category_folder, file_extension)

    # Create the category folder if it doesn't exist
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # Create the subfolder if it doesn't exist
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    # Move the file to the appropriate subfolder
    src_path = os.path.join(path, file)
    dest_path = os.path.join(subfolder_path, file)
    try:
        shutil.move(src_path, dest_path)
        print(f'Moved {src_path} to {dest_path}')
    except Exception as e:
        print(f'Error moving {src_path}: {e}')
