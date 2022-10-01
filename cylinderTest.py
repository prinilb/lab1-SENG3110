import unittest
import cylinder

class cylinderTest(unittest.TestCase):

    #passing tests
    def test_volume1(self):
        assert(cylinder.volume(10,32) == 10053.10)

    def test_surfaceArea1(self):
        assert(cylinder.surfaceArea(10,32) == 2638.94)

    #failing test
    # def test_volume2(self):
    #     assert(cylinder.volume(10,32) == 0)

    # def test_surfaceArea2(self):
    #     assert(cylinder.surfaceArea(10,32) == 0)


if __name__ == '__main__':
    unittest.main()