import unittest
import triangle

class triangleTest(unittest.TestCase):

    #passing tests
    def test_perimeter1(self):
        assert(triangle.perimeter(11,15,18) == 44.00)

    def test_semi_perimeter1(self):
        assert(triangle.semi_perimeter(11,15,18) == 22.00)

    def test_area1(self):
        assert(triangle.area(11,15,18) == 82.32)

    #failing test
    # def test_perimeter1(self):
    #     assert(triangle.perimeter(11,15,18) == 0)

    # def test_semi_perimeter1(self):
    #     assert(triangle.semi_perimeter(11,15,18) == 0)

    # def test_area1(self):
    #     assert(triangle.area(11,15,18) == 0)

if __name__ == '__main__':
    unittest.main()