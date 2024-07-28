from app.models import Expense
from app.utils.validation import validate_expense_data
from app.utils.balance_sheet import generate_balance_sheet

def add_expense(data):
    if validate_expense_data(data):
        expense = Expense.add_expense(data)
        return {"message": "Expense added successfully", "expense_id": str(expense.inserted_id)}
    return {"error": "Invalid expense data"}

def get_user_expenses(user_id):
    expenses = Expense.get_user_expenses(user_id)
    return expenses

def get_all_expenses():
    expenses = Expense.get_all_expenses()
    return expenses

def download_balance_sheet():
    balance_sheet = generate_balance_sheet()
    return balance_sheet
