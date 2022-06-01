from line import draw_pre
from line import draw_line
import unittest

class TestStringMethods(unittest.TestCase):
    # local testing
    def test_visualization(self):
        self.assertEqual(draw_line("data","data"),"data")
        self.assertEqual(draw_pre("data", "data"), "data")
    # def test_add():
    #     assert 1+1 == 2 '1+1 == 2 is right'

if __name__=="__main__":
    unittest.main()