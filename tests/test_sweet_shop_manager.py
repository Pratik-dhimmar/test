import unittest
from sweet_shop.sweet_shop_manager import SweetShopManager

class TestSweetShopManager(unittest.TestCase):
    def setUp(self):
        self.manager = SweetShopManager()

    def test_add_sweet(self):
        # Test that a sweet can be added successfully
        self.manager.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20) 
        sweets = self.manager.view_sweets() 
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0]['name'], "Kaju Katli")
        self.assertEqual(sweets[0]['id'], 1001)

if __name__ == '__main__':
    unittest.main()

# tests/test_sweet_shop_manager.py (continued)
    def test_delete_sweet_successfully(self):
        self.manager.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.manager.add_sweet(1002, "Gulab Jamun", "Milk-Based", 10, 50)
        self.assertEqual(len(self.manager.view_sweets()), 2)

        self.manager.delete_sweet(1001)
        sweets = self.manager.view_sweets()
        self.assertEqual(len(sweets), 1)
        self.assertEqual(sweets[0]['id'], 1002)

    def test_delete_non_existent_sweet_raises_error(self):
        self.manager.add_sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        with self.assertRaises(ValueError) as cm:
            self.manager.delete_sweet(9999) # Non-existent ID
        self.assertIn("Sweet with ID 9999 not found.", str(cm.exception))