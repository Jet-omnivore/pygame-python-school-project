import json
import os


def is_json_file(filename):
    return filename.split('.')[-1] == 'json'


def read_config_files(path_to_folder):
    all_configs = {}
    all_folders = os.listdir(path_to_folder)
    config_files = filter(is_json_file, all_folders)

    for file in config_files:
        file_name = file.split('.')[0]
        full_path = path_to_folder + file
        with open(full_path) as f:
            raw_data = f.read()
            data = json.loads(raw_data)
            all_configs[file_name] = data
    return all_configs


config = read_config_files('configs/')
