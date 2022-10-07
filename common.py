import os

# New website crawled saved to new folder
def create_project_dir(dir_path):
    if not os.path.exists(dir_path):
        print("Creating directory: " + dir_path)
        os.makedirs(dir_path)

# Create and queue links on a site
def create_data_files(dir_path, homepage_url):
    queue = dir_path + "/queue.txt"
    crawled = dir_path + "/crawled.txt"

    if not os.path.exists(queue):
        write_file(queue, homepage_url)
    if not os.path.exists(crawled):
        write_file(crawled, '')

# Create new file
def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()

create_project_dir("pokemon")
create_data_files("pokemon", "https://poker.com")