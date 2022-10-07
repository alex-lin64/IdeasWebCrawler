from inspect import _void
import os

# New website crawled saved to new folder
def create_project_dir(dir_path:str) -> None:
    if not os.path.exists(dir_path):
        print("Creating directory: " + dir_path)
        os.makedirs(dir_path)

# Create and queue links on a site
def create_data_files(dir_path:str, homepage_url:str) -> None:
    queue = dir_path + "/queue.txt"
    crawled = dir_path + "/crawled.txt"

    if not os.path.exists(queue):
        write_file(queue, homepage_url)
    if not os.path.exists(crawled):
        write_file(crawled, '')

# Create new file
def write_file(path:str, data:str) -> None:
    file = open(path, 'w')
    file.write(data)
    file.close()

# Write onto existing file
def append_to_file(path:str, data:str) -> None:
    with open(path, 'a') as file:
        file.write(data + '\n')

# Delete contents of a file
def delete_file_contents(path:str) -> None:
    with open(path, 'w') as file:
        pass

# Reads a file, converts each line to set items
def file_to_set(file_path:str) -> set():
    set_from_file = set()

    with open(file_path, 'rt') as file:
        for line in file:
            set_from_file.add(line.replace('\n', ''))
    return set_from_file

# Iterates through set, writes each item to a new line in given file
def set_to_file(links:str, file_path:str) -> None:
    delete_file_contents(file_path)
    for link in links:
        append_to_file(file_path, link)