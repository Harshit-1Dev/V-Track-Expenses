import unittest
from app import create_app, mongo

class ExpenseTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.db = mongo.db
        
        self.db.expenses.delete_many({})

    def test_add_expense(self):
        response = self.client.post('/expenses/', json={
            "amount": 3000,
            "participants": [
                {"user_id": "user1", "amount": 1000},
                {"user_id": "user2", "amount": 1000},
                {"user_id": "user3", "amount": 1000}
            ],
            "split_method": "equal"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Expense added successfully', response.get_json()['message'])

    def test_get_user_expenses(self):
        self.db.expenses.insert_one({
            "amount": 3000,
            "participants": [
                {"user_id": "user1", "amount": 1000},
                {"user_id": "user2", "amount": 1000},
                {"user_id": "user3", "amount": 1000}
            ],
            "split_method": "equal"
        })
        response = self.client.get('/expenses/user/user1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

if __name__ == '__main__':
    unittest.main()
