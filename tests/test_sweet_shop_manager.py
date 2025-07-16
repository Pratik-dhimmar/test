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
