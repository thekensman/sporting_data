from flask import Blueprint
from sporting_data.controllers.players._id.bio.get import Get

blueprint = Blueprint("players/_id/bio", __name__)

@blueprint.route("/players/<id>/bio", methods = ["GET"])
def get_controller(id):
    endpoint = Get(id=id)
    #Run the endpoint within the route
    return endpoint()