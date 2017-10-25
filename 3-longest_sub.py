#!/usr/bin/env python3
import unittest
import collections
import string
import random

def longest_sub(str):
    l = list(str)
    r = collections.deque()
    maxlen = 0
    for i in range(len(l)):
        if not l[i] in r:
            r.append(l[i])
        else:
            for j in range(r.index(l[i]) + 1):
                r.popleft()
            r.append(l[i])
        if len(r) > maxlen:
            maxlen = len(r)
    return maxlen

def lengthOfLongestSubstring(s):
    start = 0
    maxlen = 0
    usedChar = {}
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxlen = max(maxlen, i - start + 1)
        usedChar[s[i]] = i
    return maxlen

class _Test(unittest.TestCase):
    def test_longest_sub(self):
        a = 'abcabcbb'
        self.assertEqual(longest_sub(a), 3)
        a = 'bbbbb'
        self.assertEqual(longest_sub(a), 1)
        a = 'pwwkew'
        self.assertEqual(longest_sub(a), 3)
    def test_llengthOfLongestSubstring(self):
        a = 'abcabcbb'
        self.assertEqual(lengthOfLongestSubstring(a), 3)
        a = 'bbbbb'
        self.assertEqual(lengthOfLongestSubstring(a), 1)
        a = 'pwwkew'
        self.assertEqual(lengthOfLongestSubstring(a), 3)
    def test_longest_sub_small_size(self):
        for i in range(1000):
            rd = random.Random()
            s = []
            for i in range(10):
                s.append(rd.choice(string.ascii_lowercase))
            s = ''.join(s)
            self.assertEqual(longest_sub(s),lengthOfLongestSubstring(s))
    def test_longest_sub_midium_size(self):
        for i in range(1000):
            rd = random.Random()
            s = []
            for i in range(30):
                s.append(rd.choice(string.ascii_lowercase))
            s = ''.join(s)
            self.assertEqual(longest_sub(s),lengthOfLongestSubstring(s))
    def test_longest_sub_large_size(self):
        for i in range(1000):
            rd = random.Random()
            s = []
            for i in range(100):
                s.append(rd.choice(string.ascii_lowercase))
            s = ''.join(s)
            self.assertEqual(longest_sub(s),lengthOfLongestSubstring(s))

if __name__ == '__main__':
    unittest.main()
