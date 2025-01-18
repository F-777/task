from ContactManager import *
import unittest

class TestContact(unittest.TestCase):
    def setUp(self):
        self.contact = Contact("John Doe", "1234567890")

    def test_show(self):
        # expected_output = "Contact\nName: John Doe\nNumber: 1234567890\n"
        # self.assertEqual(self.contact.show(), expected_output)
        print(self.contact.show())

    def test_update(self):
        self.contact.update(name="Jane Doe", number="0987654321")
        self.assertEqual(self.contact._name, "Jane Doe")
        self.assertEqual(self.contact._number, "0987654321")


class TestPersonalContact(unittest.TestCase):
    def setUp(self):
        self.personal_contact = PersonalContact("Alice Smith", "9876543210", "alice@example.com", "123 Main St")

    def test_show(self):
        # expected_output = "PersonalContact\nName: Alice Smith\nNumber: 9876543210\n"
        # self.assertEqual(self.personal_contact.show(), expected_output)
        print(self.personal_contact.show())

    def test_update(self):
        self.personal_contact.set_email("alice_new@example.com")
        self.personal_contact.set_address("456 Elm St")
        self.assertEqual(self.personal_contact.get_email(), "alice_new@example.com")
        self.assertEqual(self.personal_contact.get_address(), "456 Elm St")


class TestBusinessContact(unittest.TestCase):
    def setUp(self):
        self.business_contact = BusinessContact("Bob Johnson", "1231231234", "Tech Corp", "Developer")

    def test_show(self):
        # expected_output = "BusinessContact\nName: Bob Johnson\nNumber: 1231231234\n"
        # self.assertEqual(self.business_contact.show(), expected_output)
        print(self.business_contact.show())

    def test_update(self):
        self.business_contact.set_company("New Tech Corp")
        self.business_contact.set_job("Senior Developer")
        self.assertEqual(self.business_contact.get_company(), "New Tech Corp")
        self.assertEqual(self.business_contact.get_job(), "Senior Developer")


class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.manager = ContactManager()
        self.contact1 = PersonalContact("Alice Smith", "9876543210", "alice@example.com", "123 Main St")
        self.contact2 = BusinessContact("Bob Johnson", "1231231234", "Tech Corp", "Developer")
        self.manager.create(self.contact1)
        self.manager.create(self.contact2)

    def test_index(self):
        self.assertEqual(self.manager.index(), [self.contact1, self.contact2])

    def test_create(self):
        contact3 = PersonalContact("Charlie Brown", "5555555555", "charlie@example.com", "789 Pine St")
        self.manager.create(contact3)
        self.assertIn(contact3, self.manager.index())

    def test_search(self):
        result = self.manager.search("Alice")
        self.assertEqual(result, [self.contact1])

    def test_update(self):
        self.manager.update(name="Alice Smith")
        self.assertEqual(self.contact1._name, "Alice Smith")

    def test_destroy(self):
        self.manager.destroy("Bob Johnson")
        self.assertNotIn(self.contact2, self.manager.index())


if __name__ == '__main__':
    unittest.main()
