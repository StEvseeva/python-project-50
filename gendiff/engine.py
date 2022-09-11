import json
import yaml
from yaml.loader import SafeLoader
from os.path import normpath


def run_gendiff(file_path1, file_path2):

    file1 = parse(normpath(file_path1))
    file2 = parse(normpath(file_path2))

    print(generate_diff(file1, file2))


def parse(file_path):
    format = (file_path.split('.'))[1]
    with open(file_path) as file:
        if format.lower() == 'json':
            return json.load(file)
        elif format.lower() == 'yml' or format.lower() == 'yaml':
            return yaml.load(file, Loader=SafeLoader)


def generate_diff(data1, data2):
    diff = {}

    for key in data1.keys():
        item1 = data1[key]
        if key not in data2.keys():
            diff[f'- {key}'] = item1
        elif item1 == data2[key]:
            diff[f'  {key}'] = data2.pop(key)
        else:
            diff[f'- {key}'] = item1

    if data2:
        diff.update({f'+ {key}': item for key, item in data2.items()})

    sorted_diff = dict(sorted(diff.items(), key=lambda x: x[0][2:]))

    return (str(json.dumps(sorted_diff, indent=2,
                           separators=('', ': ')))).replace('"', '')
