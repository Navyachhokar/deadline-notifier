import os

with open("file_list.txt", "w") as f:
    for root, dirs, files in os.walk(".", topdown=True):
        level = root.count(os.sep)
        indent = "    " * level
        f.write(f"{indent}{os.path.basename(root)}/\n")
        subindent = "    " * (level + 1)
        for file in files:
            f.write(f"{subindent}{file}\n")

print("✅ File list saved to file_list.txt")
