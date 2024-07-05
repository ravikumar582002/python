# This function to used to speak the print statement in python code.
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("my name is ravi kumar .my fathe name in shri bindeshwari prasad .my mother name in punam devi ")
# engine.runAndWait()




# write a python program to pront the contents of a directory using the os module . search online for the function which does that.
import os

def print_directory_contents(directory_path):
    try:
        # Get the list of entries in the directory
        entries = os.listdir(directory_path)
        
        print(f"Contents of the directory '{directory_path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
directory_path = "/" 
  # Replace with the actual directory path
print_directory_contents(directory_path)
