import os
import yaml

with open('config.yaml') as f:
    source = yaml.safe_load(f)


def make_path(values, prefix=''):
    for directory, paths in values.items():
        dir_path = os.path.join(prefix, directory)
        os.makedirs(dir_path, exist_ok=True)
        if isinstance(paths, dict):
            make_path(paths, dir_path)
        else:
            for i in paths:
                if isinstance(i, dict):
                    make_path(i, dir_path)
                elif isinstance(i, str):
                    with open(os.path.join(dir_path, f'{i}'), 'w') as _:
                        pass


make_path(source)
