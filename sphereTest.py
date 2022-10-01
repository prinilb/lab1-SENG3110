import unittest
import sphere

class sphereTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(sphere.volume(30) == 113097.34)

    def test_surfaceArea1(self):
        assert(sphere.surfaceArea(30) == 11309.73)

    #failing test
    # def test_volume2(self):
    #     assert(sphere.volume(30) == 0)

    # def test_surfaceArea2(self):
    #     assert(sphere.volume(30) == 0)

if __name__ == '__main__':
    unittest.main()