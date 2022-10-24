import json


def stylish(tree):
    print((str(json.dumps(
        tree, indent=2, separators=('', ': ')))).replace('"', ''))


def plain(tree={}, parent=[]):
    maximum = len(tree) - 1
    prev_item = None
    prev_node = None
    for key in tree.keys():
        parent.append(key[2:])
        current_node = '.'.join(parent)
        item = tree[key]
        meaning = key[0]
        value = '[complex value]' if isinstance(item, dict) else normalize_value(item)
        if meaning == ' ' and isinstance(item, dict):
            plain(item, parent)
        elif meaning == '-':
            if key != maximum:
                if prev_node:
                    print(f'''Property '{prev_node}' was removed''')
                prev_item = value
                prev_node = current_node
            else:
                print(f'''Property '{current_node}' was removed''')
        elif meaning == '+':
            if prev_node:
                if prev_node == current_node:
                    print(f'''Property '{current_node}' was updated. From {prev_item} to {value}''')
                else:
                    print(f'''Property '{prev_node}' was removed''')
                    print(f"""Property '{current_node}' was added with value: {value}""")
                prev_item = None
                prev_node = None
            else:
                print(f"""Property '{current_node}' was added with value: {value}""")
        parent.pop(-1)


def normalize_value(item):
    SPECIAL_VALUES = {False: 'false',
                      True: 'true',
                      None: 'null',
                      }
    if item in SPECIAL_VALUES.keys():
        return f"""{SPECIAL_VALUES[item]}"""
    return f"""'{item}'"""