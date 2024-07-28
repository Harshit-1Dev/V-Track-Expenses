# Daily Expenses Sharing Application

## Setup and Installation

1. **Clone the repository**
    ```bash
    git clone <repository_url>
    cd expense_sharing_app
    ```

2. **Create a virtual environment and activate it**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**
    ```bash
    python run.py
    ```

5. **Run the tests**
    ```bash
    python -m unittest discover -s app/tests
    ```

## API Endpoints

### User Endpoints

- **Create User**
    - `POST /users/`
    - Body:
    ```json
    {
        "email": "test@example.com",
        "name": "Test User",
        "mobile": "1234567890"
    }
    ```

- **Retrieve User Details**
    - `GET /users/<email>`

### Expense Endpoints

- **Add Expense**
    - `POST /expenses/`
    - Body:
    ```json
    {
        "amount": 3000,
        "participants": [
            {"user_id": "user1", "amount": 1000},
            {"user_id": "user2", "amount": 1000},
            {"user_id": "user3", "amount": 1000}
        ],
        "split_method": "equal"
    }
    ```

- **Retrieve Individual User Expenses**
    - `GET /expenses/user/<user_id>`

- **Retrieve Overall Expenses**
    - `GET /expenses/all`

- **Download Balance Sheet**
    - `GET /expenses/download`

