import unittest
from models.transaction import Transaction
from models import db, app
from uuid import uuid4
from datetime import datetime, timezone
from models.account import Account


class TransactionTest(unittest.TestCase):
    def setUp(self):
        with app.app_context():
            db.create_all()

            # Create an account for the transaction
            transaction_id = str(uuid4())
            transaction = Transaction(
                id=transaction_id,
                account_id="34d481af-ccae-4ea1-a3c0-981ba77508a7",
                transaction_type="deposit",
                amount=500,
                transaction_date=datetime.now(timezone.utc),
                description="Deposit to savings",
                status="Completed",
            )

            db.session.add(transaction)
            db.session.commit()
            self.transaction_id = transaction.id
            self.account_id = transaction.account_id  # Set the account_id here

    def test_transaction_creation(self):
        with app.app_context():
            # Create a transaction
            transaction = Transaction(
                id=str(uuid4()),  # Generate a new transaction ID
                account_id=self.account_id,
                transaction_type="deposit",
                amount=500,
                transaction_date=datetime.now(timezone.utc),
                description="Deposit to savings",
                status="Completed",
            )

            db.session.add(transaction)
            db.session.commit()

            # Retrieve the transaction from the database
            retrieved_transaction = Transaction.query.get(transaction.id)

            # Perform assertions based on your model fields
            self.assertIsNotNone(retrieved_transaction)
            self.assertEqual(retrieved_transaction.account_id, self.account_id)
            self.assertEqual(retrieved_transaction.transaction_type, "deposit")
            self.assertEqual(retrieved_transaction.amount, 500)
            # Add more assertions based on your model fields


if __name__ == "__main__":
    unittest.main()
