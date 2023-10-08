# Import the os module to interact with the operating system
import os

# Define a function named 'list_dirouter' that takes a directory path 's' as an argument
def list_dirouter(s):
    # Define a nested function named 'dir_list' to recursively list directories and files
    def dir_list(d):
        # Access the 'tab_stop' variable from the outer function
        nonlocal tab_stop
        
        # Get a list of files and directories in 'd'
        files = os.listdir(d)
        
        # Iterate through the list of files and directories
        for f in files:
            # Get the current file or directory's full path
            current_dir = os.path.join(d, f)
            
            # Check if it's a directory
            if os.path.isdir(current_dir):
                # If it's a directory, print and increase the indentation
                print('\t' * tab_stop + 'directory ' + f)
                tab_stop += 1
                
                # Recursively call 'dir_list' for the subdirectory
                dir_list(current_dir)
                
                # Decrease the indentation after returning from recursion
                tab_stop -= 1
            else:
                # If it's a file, simply print the filename
                print(f)

    # Initialize the tab_stop variable to control indentation
    tab_stop = 0
    
    # Check if the provided directory path 's' exists
    if os.path.exists(s):
        print('Directory Listing of ' + s)
        
        # Call the 'dir_list' function with the provided directory path
        dir_list(s)
    else:
        print(s + ' Directory Does not exist')

# Call the 'list_dirouter' function with a directory path
list_dirouter("E:\\GitHub Python Projects\\OS File Read Exercise 2")
