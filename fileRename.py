import os

def rename_pictures(directory, new_name_pattern):
    # Get a list of all files in the directory
    file_list = os.listdir(directory)
    
    # Iterate over each file in the directory
    for index, filename in enumerate(file_list):
        # Create a new name for the file
        new_name = new_name_pattern.format(index + 1)
        
        # Construct the full paths for the old and new names
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        print(f"Renamed {filename} to {new_name}")
        
# Specify the directory containing the pictures
directory = "directory/with/pictures"
# Specify the new name pattern
new_name_pattern = "picture_{:01d}.jpg"  # Example pattern: picture_1.jpg, picture_2.jpg, ...

# Call the function to rename the pictures
rename_pictures(directory, new_name_pattern)
