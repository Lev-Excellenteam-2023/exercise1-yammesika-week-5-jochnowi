import os


def find_files(my_path):
    match_files = []
    for match_files in os.walk(my_path):
        for file in match_files:
            if file.startswith("deep"):
                match_files.append(os.path.join(root, file))
    return match_files


path = "/path/to/your/directory"
files = find_files(path)
print(files)
