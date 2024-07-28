from app.models import User
from app.utils.validation import validate_user_data

def create_user(data):
    if validate_user_data(data):
        user = User.create_user(data)
        return {"message": "User created successfully", "user_id": str(user.inserted_id)}
    return {"error": "Invalid user data"}

def get_user(email):
    user = User.get_user_by_email(email)
    if user:
        return user
    return {"error": "User not found"}
