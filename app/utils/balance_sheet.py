from app.models import Expense

def generate_balance_sheet():
    all_expenses = Expense.get_all_expenses()
    balance_sheet = {}
    
    for expense in all_expenses:
        for participant in expense['participants']:
            user_id = participant['user_id']
            amount = participant['amount']
            if user_id not in balance_sheet:
                balance_sheet[user_id] = 0
            balance_sheet[user_id] += amount
            
    return balance_sheet
