import unittest
from models.account import Account
from models import db, app
from uuid import uuid4
from datetime import datetime, timezone


class AccountTest(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db.create_all()

            # Create a unique ID for the account
            account_id = str(uuid4())

            # Create an account
            account = Account(
                id=account_id,
                user_id="1c4d1021-f929-4fc9-9aa6-acba4f46dd37",
                email="deolaschops@gmail.com",
                account_name="Lady Bug",
                account_number="123456789",
                account_type="Savings",
                balance=1000,
                open_date=datetime.now(timezone.utc),
                status=1,
            )

            db.session.add(account)
            db.session.commit()
            self.account_id = account.id

    def test_account_creation(self):
        with app.app_context():
            account = Account.query.get(self.account_id)
            self.assertIsNotNone(account)
            self.assertEqual(
                account.user_id, "1c4d1021-f929-4fc9-9aa6-acba4f46dd37"
            )  # Make sure to set self.user_id in your UserTest
            self.assertEqual(account.email, "deolaschops@gmail.com")
            self.assertEqual(account.account_name, "Lady Bug")
            self.assertEqual(account.account_number, "123456789")
            self.assertEqual(account.account_type, "Savings")
            self.assertEqual(account.balance, 1000)
            # Add more assertions based on your model fields

    def test_account_update(self):
        with app.app_context():
            account = Account.query.get(self.account_id)
            account.account_name = "Updated Savings Account"
            db.session.commit()
            updated_account = Account.query.get(self.account_id)
            self.assertEqual(updated_account.account_name, "Updated Savings Account")

    def test_account_deletion(self):
        with app.app_context():
            account = Account.query.get(self.account_id)
            db.session.delete(account)
            db.session.commit()
            deleted_account = Account.query.get(self.account_id)
            self.assertIsNone(deleted_account)


if __name__ == "__main__":
    unittest.main()
