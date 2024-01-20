import unittest
from models.user import User
from models import db, app
from uuid import uuid4
from flask_bcrypt import Bcrypt

class UserTest(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            db.create_all()
            bcrypt = Bcrypt()

            # Hash the password before storing it
            hashed_password = bcrypt.generate_password_hash('password123').decode('utf-8')

            user = User(id=str(uuid4()), email="deo@gmail.com", fullname="joe Doe", username="sdvhf", password=hashed_password, phone=812345689, address='1234')

            db.session.add(user)
            db.session.commit()
            self.user_id = user.id

    def test_user_creation(self):
        with app.app_context():
            user = User.query.get(self.user_id)
            self.assertIsNotNone(user)
            self.assertEqual(user.email, "deo@gmail.com")
            self.assertEqual(user.fullname, "joe Doe")
            self.assertEqual(user.username, "sdvhf")
            # Check the hashed password
            bcrypt = Bcrypt()
            self.assertTrue(bcrypt.check_password_hash(user.password, 'password123'))
            self.assertEqual(user.phone, 812345689)
            self.assertEqual(user.address, '1234')

    def test_user_update(self):
        with app.app_context():
            user = User.query.get(self.user_id)
            user.email = "updated_email@gmail.com"
            db.session.commit()
            updated_user = User.query.get(self.user_id)
            self.assertEqual(updated_user.email, "updated_email@gmail.com")

    def test_user_deletion(self):
        with app.app_context():
            user = User.query.get(self.user_id)
            db.session.delete(user)
            db.session.commit()
            deleted_user = User.query.get(self.user_id)
            self.assertIsNone(deleted_user)

    def test_user_role_assignment(self):
        with app.app_context():
            user = User.query.get(self.user_id)
            user.role = 'admin'
            db.session.commit()
            updated_user = User.query.get(self.user_id)
            self.assertEqual(updated_user.role, 'admin')

    def test_user_activation_status(self):
        with app.app_context():
            user = User.query.get(self.user_id)
            self.assertTrue(user.is_active)
            user.is_active = False
            db.session.commit()
            updated_user = User.query.get(self.user_id)
            self.assertFalse(updated_user.is_active)

if __name__ == '__main__':
    unittest.main()
