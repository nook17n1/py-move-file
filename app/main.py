import os


def move_file(command: str) -> str:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, file1, file2 = parts
    if file1 == file2:
        return
    try:
        if "/" not in file2:
            os.rename(file1, file2)
        elif "/" in file2:
            new_path = os.path.dirname(file2)
            os.makedirs(new_path, exist_ok=True)
            os.replace(file1, file2)

    except FileNotFoundError:
        return "File not exist"
