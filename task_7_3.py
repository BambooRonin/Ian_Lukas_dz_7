import os
from shutil import copytree


def dir_copying():
    source = 'my_project'
    name_dir = 'templates'

    for root, dirs, files in os.walk(source):
        if root.find(name_dir) > 0 and len(files) == 0:
            copytree(os.path.join(root), name_dir,
                     dirs_exist_ok=True)


if __name__ == '__main__':
    dir_copying()
