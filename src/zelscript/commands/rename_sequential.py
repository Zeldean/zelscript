"""Sequential renamer - renames files in a directory to 001, 002, 003... format"""
import os

def rename(directory):
    """Rename files in directory to sequential format (001, 002, 003...)"""
    for (root, _, files) in os.walk(directory):
        files.sort()
        
        existing_files = set()
        for file in files:
            existing_files.add(os.path.join(root, file))

        existing_files = sorted(existing_files)

        index = 1
        for i in existing_files:
            ext = os.path.splitext(i)[1]
            new_path = os.path.join(root, f"{index:03d}{ext}")
            if i != new_path:
                if os.path.exists(new_path) and new_path not in existing_files:
                    print(f"SKIP: {new_path} already exists")
                    continue
                os.rename(i, new_path)
                print(f"{i} -> {new_path}")
            index += 1
    
