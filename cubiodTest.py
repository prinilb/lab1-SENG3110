import unittest
import cuboid

class cuboidTest(unittest.TestCase):

    #passing tests
    def test_surfaceArea1(self):
        assert(cuboid.surfaceArea(21,15,10) == 1350)

    def test_volume1(self):
        assert(cuboid.volume(21,15,10) == 3150)

    def test_latSurf1(self):
        assert(cuboid.latSurf(21,15,10) == 720)

    #failing test
    # def test_surfaceArea2(self):
    #     assert(cuboid.surfaceArea(12,15,10) == 0)

    # def test_volume2(self):
    #     assert(cuboid.surfaceArea(12,15,10) == 0)

    # def test_latSurf2(self):
    #     assert(cuboid.latSurf(12,15,10) == 0)


if __name__ == '__main__':
    unittest.main()