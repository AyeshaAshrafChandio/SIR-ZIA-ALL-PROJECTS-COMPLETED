import os

def bulk_rename():
    print("=== Bulk File Renamer ===")
    
    # Get folder path from user
    folder_path = input("Enter folder path: ")
    
    # Verify folder exists
    if not os.path.exists(folder_path):
        print("Error: Folder does not exist!")
        return
    
    # Get new name pattern
    prefix = input("Enter new file name prefix: ")
    start_num = int(input("Enter starting number: "))
    
    # Get all files in folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Rename files
    for i, filename in enumerate(files, start=start_num):
        file_ext = os.path.splitext(filename)[1]  # Get file extension
        new_name = f"{prefix}_{i}{file_ext}"
        
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")
    
    print("\nAll files renamed successfully!")

if __name__ == "__main__":
    bulk_rename()