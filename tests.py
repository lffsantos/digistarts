from question1 import run_question
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(run_question(10, [10, 10, 9, 9, 8, 8, 7, 7, 6, 6]), [6, 7, 8, 9, 10])

    def test2(self):
        self.assertEqual(run_question(5, [-1, -1, -1, -1, -1]), [-1])

    def test3(self):
        self.assertEqual(run_question(5, [-123, 123, 999, 1000, -1000]), [-1000, -123, 123, 999, 1000])

    def test4(self):
        N, K = 0, [10, 10, 9, 9, 8, 8, 7, 7, 6, 6]
        self.assertRaises(ValueError, run_question, N, K)

    def test5(self):
        N, K = 10, [-2000, 10, 9, 9, 8, 8, 7, 7, 6, 6]
        self.assertRaises(ValueError, run_question, N, K)


if __name__ == '__main__':
    unittest.main()
