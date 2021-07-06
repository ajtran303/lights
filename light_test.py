import unittest
from light import Light

class LightTest(unittest.TestCase):
    """
    - There is a light
    - It can turn on and off
    - It can shine light or not
    - When a light shines, it emits lumens
    """

    # a light exists with lumens
    # a light is unshone and does not emit lumens
    # a light turns on
    # a light is shone and emits lumens
    # a light turns off
    # a light is unshone and does not emit lumens anymore

    def setUp(self):
        """A light is initialized with lumens"""
        self.light = Light(lumens=100)

    # def tearDown(self):
        # self.light.power_off() # ?

    def test_it_exists_with_attributes(self):
        """Smoke test"""
        self.assertIsInstance(self.light, Light)
        self.assertEqual(self.light.lumens, 100)

    def test_it_does_not_shine_unless_powered(self):
        """Integration test"""
        self.assertEqual(self.light.is_on, (False))
        self.assertEqual(self.light.shine(), (0))

        self.light.power_on()
        self.assertEqual(self.light.is_on, (True))
        self.assertEqual(self.light.shine(), (100))

        self.light.power_off()
        self.assertEqual(self.light.is_on, (False))
        self.assertEqual(self.light.shine(), (0))




if __name__ == '__main__':
    unittest.main()
