import shutil 
from datetime import date 
import os 
import sys 

def take_backup(src_file_name, 
                dst_file_name=None, 
                src_dir='./', 
                dst_dir='./backups/'): 
    try: 
        
        # Extract the today's date 
        today = date.today() 
        date_format = today.strftime("%d_%b_%Y_") 

        # Create full source path
        src_path = os.path.join(src_dir, src_file_name)

        if not src_file_name: 
            print("Please specify the source file name.") 
            exit() 

        try: 
            
            # Determine destination filename 
            if dst_file_name is None or not dst_file_name: 
                dst_file_name = f"{date_format}{src_file_name}"

            # Create full destination path
            dst_path = os.path.join(dst_dir, dst_file_name)

            # Copy the file
            shutil.copy2(src_path, dst_path) 

            print("Backup Successful!") 
        except FileNotFoundError as e: 
            print(f"File not found: {src_path}. Please check the path.") 
    
        except PermissionError: 
            # Handle permission errors (optional)
            print("Error: Insufficient permissions to create backup.")

# Example usage
take_backup("GFG.txt")  # Creates backups/12_Nov_2024_GFG.txt
take_backup("data.csv", "important_data.csv", dst_dir="important_backups/")