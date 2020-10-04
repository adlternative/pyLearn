import unittest
import doctestTest

class ProductTestCase(unittest.TestCase):
    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = doctestTest.product(x, y)
                self.assertEqual(p, x*y, 'integer multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x/10
                y = y/10
                p = doctestTest.product(x, y)
                self.assertEqual(p, x*y, 'float multiplication failed')

if __name__ == '__main__':
    unittest.main()
