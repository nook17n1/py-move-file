import os


class FileNotFoundError(Exception):
    pass


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    file1, file2 = parts[1], parts[2]
    if file1 == file2:
        return
    try:
        if "/" not in file2:
            os.rename(file1, file2)
        elif "/" in file2:
            new_path = "/".join(file2.split("/")[:-1]) + "/"
            os.makedirs(new_path, exist_ok=True)
            os.replace(file1, file2)

    except FileNotFoundError:
        return "File not exist"
