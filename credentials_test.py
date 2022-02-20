import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credentials("Facebook", "12345678")

    def test_init(self):
        self.assertEqual(self.new_credential.account, "Facebook")
        self.assertEqual(self.new_credential.password, "12345678")

    def test_save_credential(self):
        """
        Test to confirm if the credential object is saved into
        the credentials list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_delete_credential(self):
        """
        Test to confirm if a credential is removed from the credentials list
        """
        self.new_credential.save_credential()  # QUESTION: Why is this here?
        test_credential = Credentials("Twitter", "12345678")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        # test if the list has one less item
        self.assertEqual(len(Credentials.credentials_list), 1)


if __name__ == '__main__':
    unittest.main()
