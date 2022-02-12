import sys, json
sys.path.append('components')
from decouple import config

def list_active_components():
    with open('template.json') as json_file:
        grid_data = json.load(json_file)
    components = [column.get('component') for row in grid_data['rows'] for column in row['columns']]
    return components

#TODO: refactor this and the similar code in ui.py to a generic get_component_callback()
def get_component_callback(component_name):
    module = __import__(component_name)
    return getattr(module, 'update', None)

def get_update_frequency(component_name):
    return config(f'{component_name}_update_interval', default=300, cast=int)

if __name__ == "__main__":
    components = list_active_components()
    for component in components:
        callback = get_component_callback(component)
        if callback:
            update_interval = get_update_frequency(component)
            print(f'{component} will update every {update_interval} seconds')
        else:
            print(f'{component} has no update callback')
