from flask import Blueprint, request, jsonify
from app.services.expense_service import add_expense, get_user_expenses, get_all_expenses, download_balance_sheet

expense_bp = Blueprint('expense_bp', __name__)

@expense_bp.route('/', methods=['POST'])
def add_expense_route():
    data = request.get_json()
    response = add_expense(data)
    return jsonify(response)

@expense_bp.route('/user/<user_id>', methods=['GET'])
def get_user_expenses_route(user_id):
    response = get_user_expenses(user_id)
    return jsonify(response)

@expense_bp.route('/all', methods=['GET'])
def get_all_expenses_route():
    response = get_all_expenses()
    return jsonify(response)

@expense_bp.route('/download', methods=['GET'])
def download_balance_sheet_route():
    response = download_balance_sheet()
    return jsonify(response)
