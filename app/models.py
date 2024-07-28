from flask_pymongo import ObjectId
from app import mongo

class User:
    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data)
    
    @staticmethod
    def get_user_by_email(email):
        return mongo.db.users.find_one({"email": email})

class Expense:
    @staticmethod
    def add_expense(data):
        return mongo.db.expenses.insert_one(data)
    
    @staticmethod
    def get_user_expenses(user_id):
        return list(mongo.db.expenses.find({"participants.user_id": user_id}))
    
    @staticmethod
    def get_all_expenses():
        return list(mongo.db.expenses.find())
