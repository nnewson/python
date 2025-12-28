import unittest

from typing import List

def pair_sum_sorted_brute_force(nums: List[int],
                                target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

def shift_zeros_to_the_end(nums: List[int]) -> None:
    left = 0
    n = len(nums)

    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

class TestTwoPointers(unittest.TestCase):
    def test_find_correct_elements(self):
        self.assertEqual(pair_sum_sorted_brute_force([-5, -2, 3, 4, 6], 7), [2,3]) 

class TestShiftZerosToEnd(unittest.TestCase):
    def test_initial_list(self):
        input = [0, 1, 0, 3, 2]
        shift_zeros_to_the_end(input)
        self.assertEqual(input, [1,3,2,0,0])

    def test_zero(self):
        input = [0]
        shift_zeros_to_the_end(input)
        self.assertEqual(input, [0])

    def test_one(self):
        input = [1]
        shift_zeros_to_the_end(input)
        self.assertEqual(input, [1])

    def test_all_zeros(self):
        input = [0, 0, 0]
        shift_zeros_to_the_end(input)
        self.assertEqual(input, [0, 0, 0])

    def test_all_non_zeros(self):
        input = [1, 3, 2]
        shift_zeros_to_the_end(input)
        self.assertEqual(input, [1, 3, 2])

    def test_already_sorted(self):
        input = [1, 1, 1, 0, 0]
        shift_zeros_to_the_end(input)
        self.assertEqual(input, [1, 1, 1, 0, 0])

    def test_oppsite_sorted(self):
        input = [0, 0, 1, 1, 1]
        shift_zeros_to_the_end(input)
        self.assertEqual(input, [1, 1, 1, 0, 0])

if __name__ == '__main__':
    unittest.main()