from flask import Blueprint, request, jsonify
from bson import json_util
import json
from app.services.user_service import create_user, get_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user_route():
    data = request.get_json()
    response = create_user(data)
    return json.loads(json_util.dumps(response))



@user_bp.route('/<email>', methods=['GET'])
def get_user_route(email):
    response = get_user(email)
    
    return json.loads(json_util.dumps(response))
