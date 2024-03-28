import sys
import re
import logging

logging.basicConfig(level=logging.DEBUG,  # Set the threshold for logging
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def is_valid_directory_name(directory_name):
    """Checks if the directory name is valid based on the specified rules.

    Args:
        directory_name (str): The directory name to check.

    Returns:
        bool: True if the directory name is valid, False otherwise.
    """
    # Allow '.', '..', and alphanumeric names
    return directory_name == '.' or directory_name == '..' or directory_name.isalnum()

def change_the_directory(current_path, new_path):
    """ This function change the directory path based on
    new path provided

    Args:
        current_path (str): The current directory path.
        new_path (str): The new directory path to change to.

    Returns:
        str: The resulting directory path after the change or an error message.
    """
    try:
        # Normalize the new path by replacing multiple slashes with a single one
        new_path = re.sub(r'/+', '/', new_path)

        # If the new path starts with '/', it's an absolute path; start from root
        if new_path.startswith('/'):
            path_components = []
        else:
            # Otherwise, start from the current directory, split into components
            path_components = current_path.strip('/').split('/')

        # Split the new path into components and process each one
        for component in new_path.split('/'):
            if component != '' and not is_valid_directory_name(component):
                return f"{component}: No such file or directory"
            if component == '..':
                # Move up to the parent directory, if not already at root
                if path_components:
                    path_components.pop()
            elif component and component != '.':
                # Add the new directory to the path, ignoring '.' (current directory)
                path_components.append(component)

        # Construct the new path from the components
        new_directory = '/' + '/'.join(path_components)

        # Handle the case where the resulting directory is root
        if not new_directory or new_directory == '/':
            return '/'

        return re.sub(r'/+', '/', new_directory)
    
    except Exception as e:
        logger.error(f"Raised an expection at change_the_directory : {e}", exc_info=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <current_directory> <new_directory>")
        sys.exit(1)
    logger.info("Started the Program to get modified path")
    current_directory = sys.argv[1]
    new_directory = sys.argv[2]
    logging.info(f"Provided Paths : {current_directory}, {new_directory}")
    result = change_the_directory(current_directory, new_directory)
    logging.info(f"Generated result path : {result}")