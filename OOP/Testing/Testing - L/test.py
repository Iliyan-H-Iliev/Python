from unittest import TestCase, main


def sum_nums(a, b):
    return a + b


class TestSumNums(TestCase):
    def test_sum_nums(self):
        result = sum_nums(1, 2)
        self.assertEqual(result, 3)

    def test_sum_nums_zero(self):
        result = sum_nums(0, 0)
        self.assertEqual(result, 0)

    def test_sum_nums_negative(self):
        result = sum_nums(-1, -2)
        self.assertEqual(result, -3)

    def test_sum_nums_float(self):
        result = sum_nums(1.5, 2.5)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    main()
