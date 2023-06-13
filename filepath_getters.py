import os

def get_file_paths(folder = './data'):
    directory = folder # Replace with your desired directory path

    file_paths = []

    # Recursively walk through the directory tree
    for root, directories, files in os.walk(directory):
        # Iterate over each file in the current directory
        for filename in files:
            # Create the full file path by joining the root path and the file name
            file_path = os.path.join(root, filename)

            file_extension = os.path.splitext(file_path)[1]
           
            if (file_extension == '.h5'):
                # Add the file path to the list
                file_paths.append(file_path)

    # Print the list of file paths
    #for file_path in file_paths:
    #    print(file_path)
    return file_paths

