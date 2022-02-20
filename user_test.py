import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Davidkiama", "12345678")

    def test_init(self):
        """
        Test case for the user class
        """
        self.assertEqual(self.new_user.username, "Davidkiama")
        self.assertEqual(self.new_user.password, "12345678")

    def test_user_password(self):
        """
        Test case to check if the password is correct
        """
        self.assertEqual(self.new_user.check_password("12345678"), True)


if __name__ == '__main__':
    unittest.main()
