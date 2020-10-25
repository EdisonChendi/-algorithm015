import unittest
from unittest.case import TestCase


def get_bit(v, n):
    return v >> n & 1


def set_bit(v, n):
    return v | (1 << n)


def clear_bit(v, n):
    return v & ~(1 << n)


def clear_lower_bits(v, n):
    return v & (~0 << n)


def get_n_bit_power(v, n):
    return v & (1 << n)


def clear_higher_bits(v, n):
    pass


def is_odd(x):
    return x & 1 == 1


def is_even(x):
    return x & 1 == 0


def divide_by_2(x):
    return x >> 1


def clear_right_most_1(x):
    return x & (x-1)


class TestCase(unittest.TestCase):

    def test_get_bit(self):
        v = 0b01010011
        self.assertEqual(get_bit(v, 0), 1)
        self.assertEqual(get_bit(v, 1), 1)
        self.assertEqual(get_bit(v, 2), 0)
        self.assertEqual(get_bit(v, 3), 0)
        self.assertEqual(get_bit(v, 4), 1)
        self.assertEqual(get_bit(v, 5), 0)
        self.assertEqual(get_bit(v, 6), 1)
        self.assertEqual(get_bit(v, 7), 0)

    def test_set_bit(self):
        v = 0b01010011
        self.assertEqual(set_bit(v, 2), 0b01010111)

    def test_clear_bit(self):
        v = 0b01010011
        self.assertEqual(clear_bit(v, 1), 0b01010001)

    def test_clear_lower_bits(self):
        v = 0b01011010
        self.assertEqual(clear_lower_bits(v, 2), 0b01011000)

    def test_get_n_bit_power(self):
        v = 0b01011010
        self.assertEqual(get_n_bit_power(v, 3), 0b1000)
        self.assertEqual(get_n_bit_power(v, 2), 0b000)

    def test_is_even_is_odd(self):
        self.assertTrue(is_odd(11))
        self.assertFalse(is_even(11))
        self.assertFalse(is_odd(12))
        self.assertTrue(is_even(12))

    def test_divide_by_2(self):
        self.assertEqual(divide_by_2(8), 4)
        self.assertEqual(divide_by_2(7), 3)

    def test_divide_by_2(self):
        self.assertEqual(divide_by_2(8), 4)
        self.assertEqual(divide_by_2(7), 3)
        self.assertEqual(divide_by_2(6), 3)
        self.assertEqual(divide_by_2(3), 1)

    def test_clear_right_most_1(self):
        v = 0b01011000
        res = 0b01010000
        self.assertEqual(clear_right_most_1(v), res)

    def test_get_0(self):
        v = 0b01011000
        self.assertEqual(v & ~v, 0)


if __name__ == "__main__":
    unittest.main()
