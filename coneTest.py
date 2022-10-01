import unittest
import cone

class coneTest(unittest.TestCase):

    #passing tests
    def test_slant1(self):
        assert(cone.slant(12,25) == 27.73)

    def test_surfaceArea1(self):
        assert(cone.surfaceArea(12,25) == 1497.82)

    def test_volume1(self):
        assert(cone.volume(12,25) == 3769.91)

    def test_latSurf1(self):
        assert(cone.latSurf(12,25) == 1045.43)

    #failing test
    # def test_slant2(self):
    #     assert(cone.slant(12,25) == 0)

    # def test_surfaceArea2(self):
    #     assert(cone.surfaceArea(12,25) == 0)

    # def test_volume2(self):
    #     assert(cone.volume(12,25) == 0)

    # def test_latSurf2(self):
    #     assert(cone.latSurf(12,25) == 0)


if __name__ == '__main__':
    unittest.main()