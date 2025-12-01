from app import app
from forms import RegisterForm
import unittest

class TestRegisterForm(unittest.TestCase):
    def setUp(self):
        app.secret_key = 'super secret key'
        app.config["WTF_CSRF_ENABLED"] = False
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_validate_password(self):
        with app.test_request_context():
            form = RegisterForm()
            form.email.data = "test@test.com"
            form.username.data = "testuser"

            # Test password length less than 8 characters
            form.password.data = "Passw1!"
            self.assertFalse(form.validate())
            self.assertIn("Password must be between 8 and 12 characters and contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%&)", form.errors["password"])

            # Test password length more than 12 characters
            form.password.data = "Password1234!"
            self.assertFalse(form.validate())
            self.assertIn("Password must be between 8 and 12 characters and contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%&)", form.errors["password"])

            # Test password without uppercase letter
            form.password.data = "password1!"
            self.assertFalse(form.validate())
            self.assertIn("Password must be between 8 and 12 characters and contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%&)", form.errors["password"])

            # Test password without lowercase letter
            form.password.data = "PASSWORD1!"
            self.assertFalse(form.validate())
            self.assertIn("Password must be between 8 and 12 characters and contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%&)", form.errors["password"])

            # Test password without number
            form.password.data = "Password!"
            self.assertFalse(form.validate())
            self.assertIn("Password must be between 8 and 12 characters and contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%&)", form.errors["password"])

            # Test password without special character
            form.password.data = "Password1"
            self.assertFalse(form.validate())
            self.assertIn("Password must be between 8 and 12 characters and contain at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%&)", form.errors["password"])

            # Test valid password
            form.password.data = "Passw1!23"
            self.assertTrue(form.validate())

if __name__ == '__main__':
    unittest.main()
