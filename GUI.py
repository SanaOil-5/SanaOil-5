# Dont run!!!!

import tkinter as tk
import subprocess
import os
import sys
import tempfile

# Function to run npm start using subprocess.Popen
def start_npm():
    try:
        # Define the directory path
        project_dir = r"C:/Users/Mrpay/OneDrive\Desktop\SanaOil/yolo-live-feed"
        
        # Ensure the directory exists
        if not os.path.isdir(project_dir):
            raise FileNotFoundError(f"The directory {project_dir} does not exist.")
        
        # Change the working directory
        os.chdir(project_dir)
        
        # Add npm's directory to the PATH explicitly
        npm_path = r"C:/Users/Mrpay/AppData/Roaming/npm"
        os.environ["PATH"] += os.pathsep + npm_path
        
        # Create a temporary file to capture output
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tempFile:
            # Run npm start using subprocess.Popen
            process = subprocess.Popen(["npm", "start"], stdout=tempFile, stderr=subprocess.PIPE, shell=True)
            
            # Wait for the process to finish
            process.wait()
            
            # Print the output from the temporary file
            tempFile.seek(0)
            print(tempFile.read())
            
            # Print any errors (if any)
            stderr_output = process.stderr.read().decode()
            if stderr_output:
                print(stderr_output)
    
    except Exception as e:
        print(f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Start NPM")

# Set window size
root.geometry("300x150")

# Add a button that triggers npm start
start_button = tk.Button(root, text="Start NPM", command=start_npm)
start_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
