import unittest
import main_12_testing1


class TestMain12Testing1(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main_12_testing1.do_stuff(test_param)
        self.assertEqual(
            result, 30, "The result should be 30 when input is 10.")

    def test_do_stuff2(self):
        test_param = "abcdef"
        result = main_12_testing1.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))


if __name__ == "__main__":
    unittest.main()
