import unittest
import equiTriangle

class equiTriangleTest(unittest.TestCase):

    #passing tests
    def test_area1(self):
        assert(equiTriangle.area(6) == 15.59)

    def test_perimeter1(self):
        assert(equiTriangle.perimeter(6) == 18.00)

    def test_semi_perimeter1(self):
        assert(equiTriangle.semi_perimeter(6) == 9.00)

    def test_altitude1(self):
        assert(equiTriangle.altitude(6) == 5.20)

    #failing test
    # def test_area2(self):
    #     assert(equiTriangle.area(6) == 0)

    # def test_perimeter2(self):
    #     assert(equiTriangle.perimeter(6) == 0)

    # def test_semi_perimeter2(self):
    #     assert(equiTriangle.semi_perimeter(6) == 0)

    # def test_altitude2(self):
    #     assert(equiTriangle.altitude(6) == 0)

if __name__ == '__main__':
    unittest.main()