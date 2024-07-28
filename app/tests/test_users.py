import unittest
from app import create_app, mongo

class UserTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.db = mongo.db
        
        self.db.users.delete_many({})

    def test_create_user(self):
        response = self.client.post('/users/', json={
            "email": "test@example.com",
            "name": "Test User",
            "mobile": "1234567890"
        })
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
        self.assertIn('User created successfully', response.get_json()['message'])

    def test_get_user(self):
        self.db.users.insert_one({
            "email": "test@example.com",
            "name": "Test User",
            "mobile": "1234567890"
        })
        response = self.client.get('/users/test@example.com')
        self.assertEqual(response.status_code, 200)
        print(response.get_json())
        self.assertEqual(response.get_json()['email'], 'test@example.com')

if __name__ == '__main__':
    unittest.main()
