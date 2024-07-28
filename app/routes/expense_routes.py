from flask import Blueprint, request, jsonify
from bson import json_util
import json

from app.services.expense_service import add_expense, get_user_expenses, get_all_expenses, download_balance_sheet

expense_bp = Blueprint('expense_bp', __name__)

@expense_bp.route('/', methods=['POST'])
def add_expense_route():
    data = request.get_json()
    response = add_expense(data)
    #return jsonify(response)
    return json.loads(json_util.dumps(response))

@expense_bp.route('/user/<user_id>', methods=['GET'])
def get_user_expenses_route(user_id):
    response = get_user_expenses(user_id)[0]
    #return jsonify(response)
    #print (response)
    return json.loads(json_util.dumps(response))

@expense_bp.route('/all', methods=['GET'])
def get_all_expenses_route():
    response = get_all_expenses()
    #return jsonify(response)
    return json.loads(json_util.dumps(response))

@expense_bp.route('/download', methods=['GET'])
def download_balance_sheet_route():
    response = download_balance_sheet()
    #return jsonify(response)
    return json.loads(json_util.dumps(response))
