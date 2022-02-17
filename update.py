import sys, json
from importlib import import_module

def list_active_components():
    with open('services.json') as json_file:
        grid_data = json.load(json_file)
    services = [(row.get('service'), row.get('update_interval_seconds', 0)) for row in grid_data['services'] if row.get('service')]
    return services

#TODO: refactor this and the similar code in ui.py to a generic get_component_callback()
def get_update_callback(component_name):
    module = import_module('services.' + component_name)
    return getattr(module, 'update', None)

if __name__ == "__main__":
    components = list_active_components()
    for component, update_interval in components:
        callback = get_update_callback(component)
        if callback:
            if update_interval:
                print(f'{component} will update every {update_interval} seconds.')
            else:
                print(f'{component} has an update callback, but is not set to update at any interval.')

        else:
            print(f'{component} has no update callback available.')
