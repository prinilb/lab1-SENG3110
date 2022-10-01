import unittest
import trapezoid

class trapezoidTest(unittest.TestCase):

    #passing tests
    def test_area1(self):
        assert(trapezoid.area(26,20,15) == 345.00)

    def test_median1(self):
        assert(trapezoid.median(26,20,15) == 23.00)

    #failing test
    # def test_area2(self):
    #     assert(trapezoid.area(26,20,15) == 0)

    # def test_median2(self):
    #     assert(trapezoid.median(26,20,15) == 0)

if __name__ == '__main__':
    unittest.main()