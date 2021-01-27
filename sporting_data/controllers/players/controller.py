from flask import request, Blueprint
from sporting_data.controllers.players.get import Get

blueprint = Blueprint("players", __name__)

@blueprint.route("/players", methods = ["GET"])
def get_controller():
    endpoint = Get()
    #Run the endpoint within the route
    return endpoint()