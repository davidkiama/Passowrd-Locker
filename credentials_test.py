import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credentials("Facebook", "12345678")

    def test_init(self):
        """
        Test to confirm if the object is initialized properly
        """
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
        """
        TearDown method that does clean up after each test case has run.
        """
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

    def test_display_credentials(self):
        """
        Test to confirm if the list of credentials is the same as the 
        the one returned by display_credentials function 
        """
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)

    def test_find_by_account(self):
        """
        Test to confirm if the find_by_account method returns the correct credential
        """
        self.new_credential.save_credential()
        test_credential = Credentials("Twitter", "12345678")
        test_credential.save_credential()

        found_credential = Credentials.find_by_account("Twitter")

        self.assertEqual(found_credential.password, test_credential.password)


if __name__ == '__main__':
    unittest.main()
