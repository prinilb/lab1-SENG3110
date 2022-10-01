import unittest
import cube

class cubeTest(unittest.TestCase):

    #passing tests
    def test_surfaceArea1(self):
        assert(cube.surfaceArea(7) == 294.00)

    def test_volume1(self):
        assert(cube.volume(7) == 343.00)

    def latSurf1(self):
        assert(cube.latSurf(7) == 196.00)

    #failing test
    # def test_surfaceArea2(self):
    #     assert(cube.surfaceArea(7) == 0)

    # def test_volume2(self):
    #     assert(cube.volume(7) == 0)

    # def latSurf2(self):
    #     assert(cube.latSurf(7) == 0)

if __name__ == '__main__':
    unittest.main()