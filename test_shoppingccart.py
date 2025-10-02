import unittest
from shoppingcart import ShoppingCart, Item
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    def test_AddItem(self):
        item = Item("Book", 12.99)
        self.cart.AddItem(item)
        self.assertIn(item, self.cart.items)
    def test_RemoveItem(self):
        item = Item("Book", 12.99)
        self.cart.AddItem(item)
        self.cart.RemoveItem(item)
        self.assertNotIn(item, self.cart.items)
    def test_TotalPrice(self):
        item1 = Item("Book", 12.99)
        item2 = Item("Pen", 1.99)
        self.cart.AddItem(item1)
        self.cart.AddItem(item2)
        self.assertEqual(self.cart.TotalPrice(), 14.98)
if __name__ == '__main__':
    unittest.main()