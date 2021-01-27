from flask import Flask, Blueprint
import os
import importlib
from sporting_data import controllers

def path_to_package(path):
    sporting_data_prefix = "sporting_data"
    package_path = path[path.rfind(sporting_data_prefix):]
    #replace slashes with linux, replace backslashes with windows
    return package_path.replace("/",".").replace("\\", ".")

def get_blueprints(package):
    #Finds all blueprints residing in files named "controller.py" under the given directory
    for controller_file in [os.path.join(dp, f) for dp, dn, filenames in os.walk(package.__path__[0]) for f in filenames if os.path.splitext(f)[0] == 'controller']:
        blueprint = getattr(importlib.import_module(path_to_package(controller_file).replace(".pyc", "").replace(".py", "")), "blueprint", None)
        if isinstance(blueprint, Blueprint):
            yield blueprint

def register_blueprints(app, package):
    for blueprint in get_blueprints(package):
        app.register_blueprint(blueprint)

"""Construct the core application."""
app = Flask(__name__, instance_relative_config=False)

app.url_map.strict_slashes = False

register_blueprints(app, controllers,)

if __name__ == "__main__":

    #debug=True
    app.run()
