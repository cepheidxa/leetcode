#!/usr/bin/env python3
import unittest
import random

def two_sum(l, num):
    length = len(l)
    l = zip(l, range(length))
    l = sorted(l)
    j = length - 1
    for i in range(length):
        while l[j][0] + l[i][0] > num and j > i:
            j -= 1
        if i == j:
            return None
        if l[j][0] + l[i][0] == num:
            if l[i][1] > l[j][1]:
                return [l[j][1], l[i][1]]
            else:
                return [l[i][1], l[j][1] ]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, first in enumerate(nums):
            second = target - first
            if second in nums[i+1:]:
                i2 = nums[i+1:].index(second) + i + 1
                return [i, i2]
        return None
            
class Test(unittest.TestCase):
    def test_two_sum(self):
        a = two_sum([3,3], 6)
        self.assertEqual(a, [0, 1])
        a = two_sum([5, 8, 2, 7, 11, 15], 9)
        self.assertEqual(a, [2,3])
        a = two_sum([1, 5, 2, 3, 5, 10], 15)
        self.assertEqual(a, [1,5])
        a = two_sum(range(100000), 200000)
        self.assertEqual(a, None)
        a = two_sum([1, 5, 2, 3, 5, 10], 20)
        self.assertEqual(a, None)
        a = two_sum([1, 5, 2, 3, 5, 10], 14)
        self.assertEqual(a, None)
    def test_twoSum(self):
        s = Solution()
        a = s.twoSum([3,3], 6)
        self.assertEqual(a, [0, 1])
        a = s.twoSum([5, 8, 2, 7, 11, 15], 9)
        self.assertEqual(a, [2,3])
        a = s.twoSum([1, 5, 2, 3, 5, 10], 15)
        self.assertEqual(a, [1,5])
        a = s.twoSum(range(100000), 200000)
        self.assertEqual(a, None)
        a = s.twoSum([1, 5, 2, 3, 5, 10], 20)
        self.assertEqual(a, None)
        a = s.twoSum([1, 5, 2, 3, 5, 10], 14)
        self.assertEqual(a, None)
    def test_two_sum_rand(self):
        rd = random.Random()
        s = Solution()
        for i in range(1000):
            a = []
            for j in range(1000):
                a.append(rd.randint(1, 100))
            num = rd.randint(1, 120)
            v1 = two_sum(a, num)
            v2 = s.twoSum(a, num)
            if v1 or v2:
                self.assertEqual(a[v1[0]] + a[v1[1]], num)
                self.assertEqual(a[v2[0]] + a[v2[1]], num)
            else:
                self.assertEqual(v1, v2)
    
if __name__ == '__main__':
    unittest.main()
