def validate_user_data(data):
    required_fields = ["email", "name", "mobile"]
    for field in required_fields:
        if field not in data:
            return False
    return True

def validate_expense_data(data):
    required_fields = ["amount", "participants", "split_method"]
    for field in required_fields:
        if field not in data:
            return False
    if data['split_method'] == 'percentage':
        total_percentage = sum(participant['percentage'] for participant in data['participants'])
        if total_percentage != 100:
            return False
    return True
