from flask import Blueprint
from sporting_data.controllers.players._id.stats.get import Get

blueprint = Blueprint("players/_id/stats", __name__)

@blueprint.route("/players/<id>/stats", methods = ["GET"])
def get_controller(id):
    endpoint = Get(id=id)
    #Run the endpoint within the route
    return endpoint()