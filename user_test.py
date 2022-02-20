import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Davidkiama", "12345678")

    def test__init(self):
        """
        Test case for the user class
        """
        self.assertEqual(self.new_user.username, "Davidkiama")
        self.assertEqual(self.new_user.password, "12345678")


if __name__ == '__main__':
    unittest.main()
